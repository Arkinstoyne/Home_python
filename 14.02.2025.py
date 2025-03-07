from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
import asyncio
import json
import random

app = FastAPI()

# Список пользователей с их статусами (True - онлайн, False - офлайн)
users = {
    "user1": True,
    "user2": False,
    "user3": True,
    "user4": False,
    "user5": True
}

# Главная страница с отображением пользователей
@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Статус пользователей</title>
        <style>
            .online { color: green; }
            .offline { color: red; }
        </style>
    </head>
    <body>
        <h1>Статус пользователей</h1>
        <ul id="userList"></ul>

        <script>
            const eventSource = new EventSource("/sse");

            eventSource.onmessage = function(event) {
                const users = JSON.parse(event.data);
                let userListHTML = "";
                for (let user in users) {
                    let statusClass = users[user] ? "online" : "offline";
                    userListHTML += `<li class="\${statusClass}">\${user} - \${users[user] ? "Онлайн 🟢" : "Офлайн 🔴"}</li>`;
                }
                document.getElementById("userList").innerHTML = userListHTML;
            };
        </script>
    </body>
    </html>
    """

# SSE-поток для обновления статуса пользователей
@app.get("/sse")
async def sse():
    async def event_stream():
        while True:
            # Симуляция изменения статуса пользователей (рандомно)
            for user in users.keys():
                users[user] = random.choice([True, False])
            yield f"data: {json.dumps(users)}\n\n"
            await asyncio.sleep(5)  # Обновление каждые 5 секунд

    return StreamingResponse(event_stream(), media_type="text/event-stream")
