from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import os
import asyncio
import random

app = FastAPI()

# Подключаем папку images как статические файлы
app.mount("/images", StaticFiles(directory="images"), name="images")

# Получаем список изображений
IMAGE_FOLDER = "images"
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.jpg', '.png', '.jpeg'))]


# Главная страница
@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI SSE Image Update</title>
    </head>
    <body>
        <h1>Обновление изображения через SSE</h1>
        <img id="image" src="/images/img1.jpg" alt="Random Image" width="500">

        <script>
            const eventSource = new EventSource("/sse");
            eventSource.onmessage = function(event) {
                document.getElementById("image").src = "/images/" + event.data;
            };
        </script>
    </body>
    </html>
    """


# SSE поток для обновления изображения
@app.get("/sse")
async def sse():
    async def event_stream():
        while True:
            image_name = random.choice(image_files)
            yield f"data: {image_name}\n\n"
            await asyncio.sleep(7)  # Обновление каждые 7 секунд

    return StreamingResponse(event_stream(), media_type="text/event-stream")
