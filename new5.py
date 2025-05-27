from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# Конфигурация базы данных (SQLite для простоты)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)

# Создаем класс модели — например, "User"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Инициализируем Flask-Admin
admin = Admin(app, name='Моя админка', template_mode='bootstrap4')

# Регистрируем модель в админке
admin.add_view(ModelView(User, db.session))

@app.route('/')
def index():
    return '<h1>Главная страница</h1><p>Перейдите в <a href="/admin/">админку</a></p>'

if __name__ == "__main__":
    # Создаем таблицы (если еще нет)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
