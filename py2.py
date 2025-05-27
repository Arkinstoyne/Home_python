from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import qrcode
import uuid
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Папка для QR-кодов
if not os.path.exists("qrcodes"):
    os.makedirs("qrcodes")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def generate_qr(request: Request, text: str = Form(...)):
    filename = f"qrcodes/{uuid.uuid4().hex}.png"
    img = qrcode.make(text)
    img.save(filename)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "qr_image": "/" + filename,
        "download_link": "/" + filename
    })

app.mount("/qrcodes", StaticFiles(directory="qrcodes"), name="qrcodes")



<!DOCTYPE html>
<html>
<head>
    <title>QR Code Generator</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; }
        input { padding: 10px; width: 300px; font-size: 16px; }
        button { padding: 10px 20px; font-size: 16px; background: #007BFF; color: white; border: none; }
        img { margin-top: 20px; }
        a { display: block; margin-top: 10px; color: #007BFF; }
    </style>
</head>
<body>
    <h1>QR Code Generator</h1>
    <form method="post">
        <input name="text" placeholder="Enter text or URL" required>
        <br><br>
        <button type="submit">Generate</button>
    </form>

    {% if qr_image %}
        <img src="{{ qr_image }}" alt="QR Code" width="250">
        <a href="{{ download_link }}" download>Download</a>
    {% endif %}
</body>
</html>