# Personalized AI Study Assistant

## Project Overview
This project is a web-based AI study assistant that provides personalized explanations based on a student’s profile. It adapts responses according to the user’s major, academic level, and preferred learning style.

The system supports:
- Personalized explanations
- Follow-up questions (conversation memory)
- Basic tool usage (calculator for math problems)

---

##  Architecture

The system consists of two main components:

### Backend (FastAPI)
- Handles API requests
- Processes user input
- Maintains conversation history
- Integrates AI response generation
- Includes a calculator tool for math questions

### Frontend (HTML + JavaScript)
- Simple user interface
- Sends user input to backend
- Displays AI responses
- Supports multi-turn conversations

---

##How to Setup

### 1. Clone the repository

git clone <your-repo-url>
cd personalized-ai-study-assistant

### 2. Setup backend

cd backend  
python -m venv venv  
venv\Scripts\activate   (Windows)  
pip install -r requirements.txt  

### 3. Run the server

python -m uvicorn app.main:app --reload  

Server will run at:  
http://127.0.0.1:8000  

### 4. Open frontend

Open the file:  
Frontend/index.html  in your browser

## Features

### Personalized Responses
The system adapts answers based on:
- Major
- Academic year
- Learning style

### Conversation Memory
The assistant remembers previous messages and supports follow-up questions.

### Calculator Tool
The system detects math expressions and computes answers automatically.

## Test Cases

### Test 1: Basic Question
Explain photosynthesis

### Test 2: Follow-up Question
Make it simpler

### Test 3: Math Tool
What is 6 * 3 + 22?