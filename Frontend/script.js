async function sendQuestion() {
    const major = document.getElementById("major").value;
    const year = document.getElementById("year").value;
    const style = document.getElementById("style").value;
    const question = document.getElementById("question").value;

    if (!question.trim()) {
        alert("Please enter a question.");
        return;
    }

    const chatBox = document.getElementById("chatBox");

    // 先把 user 問題加到畫面
    const userMessage = document.createElement("div");
    userMessage.innerHTML = `<strong>User:</strong> ${question}`;
    chatBox.appendChild(userMessage);

    const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            major: major,
            year: year,
            learning_style: style,
            question: question
        })
    });

    const data = await response.json();

    // 再把 AI 回答加到畫面
    const aiMessage = document.createElement("div");
    aiMessage.innerHTML = `<strong>AI:</strong><br>${data.answer.replace(/\n/g, "<br>")}<br><br>`;
    chatBox.appendChild(aiMessage);

    // 清空問題框，方便追問
    document.getElementById("question").value = "";
}

async function resetConversation() {
    await fetch("http://127.0.0.1:8000/reset", {
        method: "POST"
    });

    document.getElementById("chatBox").innerHTML = "";
}