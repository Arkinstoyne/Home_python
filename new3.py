import requests
from bs4 import BeautifulSoup

def get_usd_rate():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    response.encoding = 'windows-1251'  # кодировка сайта ЦБ РФ

    soup = BeautifulSoup(response.text, "xml")
    # Найдём тег, где ID валюта USD — это 'R01235'
    usd = soup.find("Valute", ID="R01235")
    if usd:
        value = usd.Value.text
        # В ЦБ РФ используется запятая в числе, заменим её на точку
        value = value.replace(',', '.')
        return float(value)
    return None



from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")







from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def get_usd_rate():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    response.encoding = 'windows-1251'

    soup = BeautifulSoup(response.text, "xml")
    usd = soup.find("Valute", ID="R01235")
    if usd:
        value = usd.Value.text.replace(',', '.')
        return float(value)
    return None

def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

@app.route('/')
def index():
    usd_rate = get_usd_rate()
    current_time = get_current_time()
    return render_template("index.html", usd_rate=usd_rate, current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)




