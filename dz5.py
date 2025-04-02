/* static/styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 0;
}
.header {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    text-align: center;
}
.container {
    margin: 20px auto;
    width: 80%;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
}
.button {
    background-color: #4CAF50;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.button:hover {
    background-color: #45a049;
}

#

<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}TaskManagementSystem{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="header">
        <h1>TaskManagementSystem</h1>
    </div>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Пример страницы обратной связи
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    # Только для авторизованных пользователей (проверяем сессии)
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        message = request.form['message']
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (user_id, message) VALUES (?, ?)', (session['user_id'], message))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('feedback.html')


# Пример шаблона feedback.html
# templates/feedback.html
"""
{% extends 'base.html' %}
{% block title %}Обратная связь{% endblock %}
{% block content %}
<h2>Обратная связь</h2>
<form method="post">
    <textarea name="message" rows="5" cols="50" placeholder="Ваше сообщение"></textarea><br>
    <button type="submit" class="button">Отправить</button>
</form>
{% endblock %}
"""
