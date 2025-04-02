from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('contacts.db')  # Открываем базу данных contacts.db
    conn.row_factory = sqlite3.Row  # Позволяет обращаться к столбцам по названию
    return conn


# Главная страница с отображением списка контактов
@app.route('/')
def index():
    conn = get_db_connection()
    contacts = conn.execute('SELECT * FROM contacts').fetchall()  # Запрос всех контактов
    conn.close()
    return render_template('index.html', contacts=contacts)  # Передаём контакты в шаблон


# Добавление нового контакта
@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']

    if name and phone:  # Проверяем, что поля не пустые
        conn = get_db_connection()
        conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
        conn.commit()  # Сохраняем изменения
        conn.close()

    return redirect(url_for('index'))  # Перенаправляем пользователя на главную страницу
