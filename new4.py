from flask import Flask, Blueprint, render_template_string

app = Flask(__name__)

# Создаем Blueprint
my_blueprint = Blueprint('my_blueprint', __name__)

# Добавляем маршрут в Blueprint
@my_blueprint.route('/hello')
def hello():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Страница Hello</title>
    </head>
    <body>
        <h1>Привет из Blueprint!</h1>
        <p>Это страница, возвращаемая функцией внутри Blueprint.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

# Регистрируем Blueprint в приложении
app.register_blueprint(my_blueprint, url_prefix='/mybp')

@app.route('/')
def index():
    return """
    <h1>Главная страница</h1>
    <p>Перейдите по адресу <a href="/mybp/hello">/mybp/hello</a> чтобы проверить Blueprint.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
