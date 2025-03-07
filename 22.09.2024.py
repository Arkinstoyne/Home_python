# 1. Функция подсчета периметра прямоугольника
def rectangle_perimeter(width, height):
    return 2 * (width + height)

# 2. Функция возведения числа в степень
def power(number, degree):
    return number ** degree

# 3. Функция подсчета количества слов в тексте
def word_count(text):
    return len(text.split())

# 4. Функция вычисления среднего арифметического бесконечного количества чисел
def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0  # Проверяем, есть ли числа