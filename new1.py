from fastapi import UploadFile
import uuid

def add_product(file: UploadFile):
    # 1. Вывести в консоль тип файла
    print(f"Тип файла: {type(file)}")  # Обычно <class 'fastapi.datastructures.UploadFile'>

    # Получить оригинальное имя и расширение
    original_filename = file.filename
    print(f"Оригинальное имя файла: {original_filename}")

    # 3. Получить расширение файла и вывести в консоль
    extension = original_filename.split('.')[-1] if '.' in original_filename else ''
    print(f"Расширение файла: {extension}")

    # 2. Создать новое имя файла через uuid, оставить расширение
    new_filename = f"{uuid.uuid4().hex}.{extension}"
    print(f"Новое имя файла: {new_filename}")

    # Здесь далее можешь сохранить файл с новым именем, например:
    # with open(f"/path/to/save/{new_filename}", "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)

    return {"new_filename": new_filename}
