from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Главная</title>
    </head>
    <body>
        <h1>Добро пожаловать в FastAPI!</h1>
        <p>Куки установлены: model_user = fastapi_user</p>
    </body>
    </html>
    """
    response = Response(content=html_content, media_type="text/html")
    response.set_cookie(key="model_user", value="fastapi_user")  # Устанавливаем куки
    return response

