from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Подключение к MongoDB (замени на свои данные)
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
users_collection = db["users"]


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]

        # Сохраняем пользователя в MongoDB
        users_collection.insert_one({
            "username": username,
            "email": email
        })

        return redirect(url_for("users"))

    return render_template("register.html")




<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Регистрация</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required><br><br>
        <input type="email" name="email" placeholder="Email" required><br><br>
        <button type="submit">Зарегистрироваться</button>
    </form>
</body>
</html>





<!DOCTYPE html>
<html>
<head>
    <title>Пользователи</title>
</head>
<body>
    <h1>Список пользователей из MongoDB</h1>
    <ul>
        {% for user in users %}
            <li>{{ user['username'] }} — {{ user['email'] }}</li>
        {% endfor %}
    </ul>
    <a href="/register">Добавить пользователя</a>
</body>
</html>