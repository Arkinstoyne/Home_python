flask_project/
│── app.py             # Основной сервер
│── templates/
│   ├── index.html     # HTML-файл для отображения данных
│── static/
│   ├── styles.css     # CSS-файл


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome/<username>')
def welcome(username):
    employees = [
        {"name": "Иван Петров", "position": "Менеджер"},
        {"name": "Мария Смирнова", "position": "Бухгалтер"},
        {"name": "Алексей Иванов", "position": "Разработчик"},
    ]
    return render_template("index.html", username=username, employees=employees)

if __name__ == '__main__':
    app.run(debug=True)

< !DOCTYPE
html >
< html
lang = "ru" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Добро
пожаловать < / title >
< link
rel = "stylesheet"
href = "{{ url_for('static', filename='styles.css') }}" >
< / head >
< body >
< div


class ="container" >

< h1 > Добро
пожаловать, {{username | upper}}! < / h1 >

< h2 > Список
сотрудников: < / h2 >
< div


class ="employee-list" >


{ %
for employee in employees %}
< div


class ="card" >

< h3 > {{employee.name}} < / h3 >
< p > Должность: {{employee.position}} < / p >
< / div >
{ % endfor %}
< / div >
< / div >
< / body >
< / html >


