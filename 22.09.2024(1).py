def filter_students(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        students = file.readlines()

    with open(output_file, "w", encoding="utf-8") as file:
        for student in students:
            parts = student.strip().split()  # Разделяем строку по пробелам
            name, grades = parts[0], list(map(float, parts[1:]))  # Имя и оценки
            if sum(grades) / len(grades) > 4.0:  # Считаем средний балл
                file.write(student)  # Записываем строку в новый файл

# Использование
filter_students("students.txt", "filtered_students.txt")




import os
import shutil
from datetime import datetime

def backup_txt_files():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Формат даты и времени
    for file in os.listdir():
        if file.endswith(".txt") and os.path.isfile(file):  # Проверяем, является ли это .txt файлом
            new_name = f"{file[:-4]}_{current_time}.txt"  # Меняем имя файла
            shutil.copy(file, new_name)  # Создаем копию

# Использование
backup_txt_files()
