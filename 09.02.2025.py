from fastapi import FastAPI, HTTPException
from pony.orm import Database, Required, Set, db_session, select

app = FastAPI()

# Подключаем БД SQLite
db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

# Определяем модели
class User(db.Entity):
    name = Required(str, unique=True)
    cars = Set("Car")  # Связь "один ко многим"

class Car(db.Entity):
    brand = Required(str)
    model = Required(str)
    user = Required(User)  # Связь с пользователем

db.generate_mapping(create_tables=True)

# Роут: Создать пользователя
@app.post("/create_user")
@db_session
def create_user(name: str):
    if User.get(name=name):
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    user = User(name=name)
    return {"message": "Пользователь создан", "user_id": user.id}

# Роут: Удалить пользователя
@app.delete("/delete_user/{user_id}")
@db_session
def delete_user(user_id: int):
    user = User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    user.delete()
    return {"message": "Пользователь удален"}

# Роут: Найти пользователя по имени
@app.get("/find_user/{name}")
@db_session
def find_user(name: str):
    user = User.get(name=name)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"user_id": user.id, "name": user.name}

# Роут: Добавить авто пользователю
@app.post("/add_car")
@db_session
def add_car(user_id: int, brand: str, model: str):
    user = User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    car = Car(brand=brand, model=model, user=user)
    return {"message": "Автомобиль добавлен", "car_id": car.id}

# Роут: Получить все автомобили пользователя
@app.get("/get_user_cars/{user_id}")
@db_session
def get_user_cars(user_id: int):
    user = User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"user": user.name, "cars": [{"brand": car.brand, "model": car.model} for car in user.cars]}

# Запуск сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
