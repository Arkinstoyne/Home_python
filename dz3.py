import threading
import random

# ЗАДАНИЕ 1.
# Пользователь вводит значения списка, затем запускаются два потока:
# - Первый поток 5 раз находит максимум и выводит его.
# - Второй поток 5 раз находит минимум и выводит его.
# Результаты выводятся поочерёдно.
def task1():
    numbers_str = input("Задание 1. Введите числа через пробел: ")
    try:
        numbers = list(map(float, numbers_str.split()))
    except ValueError:
        print("Ошибка преобразования чисел.")
        return

    # События для синхронизации: max_thread начинает первым
    event_max = threading.Event()
    event_min = threading.Event()
    event_max.set()  # устанавливаем событие, чтобы максимум начинал

    def max_thread():
        for _ in range(5):
            event_max.wait()  # ожидаем сигнала
            maximum = max(numbers)
            print("Максимум:", maximum)
            event_max.clear()  # сбрасываем событие после выполнения
            event_min.set()    # сигнализируем второму потоку

    def min_thread():
        for _ in range(5):
            event_min.wait()  # ожидаем сигнала
            minimum = min(numbers)
            print("Минимум:", minimum)
            event_min.clear()  # сбрасываем событие после выполнения
            event_max.set()    # сигнализируем первому потоку

    t1 = threading.Thread(target=max_thread)
    t2 = threading.Thread(target=min_thread)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Задание 1 выполнено.\n")


# ЗАДАНИЕ 2.
# Пользователь вводит значения списка, затем запускаются два потока:
# - Первый поток 5 раз находит сумму элементов списка и выводит её.
# - Второй поток 5 раз находит среднеарифметическое значение и выводит его.
# Результаты выводятся поочерёдно.
def task2():
    numbers_str = input("Задание 2. Введите числа через пробел: ")
    try:
        numbers = list(map(float, numbers_str.split()))
    except ValueError:
        print("Ошибка преобразования чисел.")
        return

    if not numbers:
        print("Список пуст.")
        return

    event_sum = threading.Event()
    event_avg = threading.Event()
    event_sum.set()  # первым будет поток суммы

    def sum_thread():
        for _ in range(5):
            event_sum.wait()
            s = sum(numbers)
            print("Сумма:", s)
            event_sum.clear()
            event_avg.set()

    def avg_thread():
        for _ in range(5):
            event_avg.wait()
            avg = sum(numbers) / len(numbers)
            print("Среднее арифметическое:", avg)
            event_avg.clear()
            event_sum.set()

    t1 = threading.Thread(target=sum_thread)
    t2 = threading.Thread(target=avg_thread)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Задание 2 выполнено.\n")


# ЗАДАНИЕ 3.
# При старте приложения запускаются три потока:
# - Первый поток заполняет список случайными числами.
# - Два других потока ждут завершения заполнения.
#   После заполнения один поток находит сумму, другой — среднее значение.
# Результаты выводятся на экран.
def task3():
    numbers = []
    fill_done = threading.Event()

    def fill_thread():
        # Заполним список 10 случайными числами от 0 до 100
        for _ in range(10):
            numbers.append(random.randint(0, 100))
        print("Список заполнен случайными числами.")
        fill_done.set()  # сигнализируем, что список заполнен

    def sum_thread():
        fill_done.wait()  # ожидаем заполнения списка
        s = sum(numbers)
        print("Сумма элементов списка:", s)

    def avg_thread():
        fill_done.wait()  # ожидаем заполнения списка
        avg = sum(numbers) / len(numbers) if numbers else 0
        print("Среднее значение списка:", avg)

    t_fill = threading.Thread(target=fill_thread)
    t_sum = threading.Thread(target=sum_thread)
    t_avg = threading.Thread(target=avg_thread)

    t_fill.start()
    t_sum.start()
    t_avg.start()

    t_fill.join()
    t_sum.join()
    t_avg.join()

    print("Полученный список:", numbers)
    print("Задание 3 выполнено.\n")


# Меню для выбора задания
def main():
    while True:
        print("Выберите задание:")
        print("1. Поиск максимума и минимума в списке (поочерёдно)")
        print("2. Вычисление суммы и среднего арифметического (поочерёдно)")
        print("3. Заполнение списка случайными числами и вычисление суммы и среднего")
        print("4. Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            break
        else:
            print("Некорректный ввод, попробуйте снова.\n")

if __name__ == "__main__":
    main()
