from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os
import re

def calculate_expression(expr: str):
    # numbers only
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expr):
        return None
    try:
        return eval(expr)
    except:
        return None

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation_history = []

class AskRequest(BaseModel):
    major: str
    year: str
    learning_style: str
    question: str


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.post("/ask")
def ask_question(data: AskRequest):
    global conversation_history

    import re

    user_prompt = data.question

    # Calculator
        
    if any(op in user_prompt for op in ["+", "-", "*", "/"]):
        try:
            expression = user_prompt.replace("What is", "").replace("?", "").strip()
            result = eval(expression)

            answer = (
                f"Explanation: I used a calculator tool to compute the result.\n\n"
                f"Example: {expression} = {result}\n\n"
                f"Short Summary: The answer is {result}."
            )

            conversation_history.append({"role": "user", "content": user_prompt})
            conversation_history.append({"role": "assistant", "content": answer})

            return {"answer": answer}

        except:
            pass

    #Flow
    system_prompt = f"""
Your academic study assistant.

Student Profile:
- Major: {data.major}
- Year: {data.year}
- Learning Style: {data.learning_style}

Respond with:
- Explanation
- Example
- Short Summary
"""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(conversation_history)
    messages.append({"role": "user", "content": user_prompt})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )

        answer = response.choices[0].message.content

    except Exception as e:
        print(" API error:", e)
        answer = (
            "Explanation: fallback response. Quota exceed\n\n"
            "Example: The system is currently using a default explanation.\n\n"
            "Short Summary: API quota exceeded, using fallback."
        )

    conversation_history.append({"role": "user", "content": user_prompt})
    conversation_history.append({"role": "assistant", "content": answer})

    return {"answer": answer}

@app.post("/reset")
def reset_conversation():
    global conversation_history
    conversation_history = []
    return {"message": "Conversation history cleared"}