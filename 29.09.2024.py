class Car:
    def __init__(self, mass, km, power, speed, brand):
        self.mass = mass  # Масса автомобиля (кг)
        self.km = km  # Пробег (км)
        self.power = power  # Мощность (л.с.)
        self.speed = speed  # Максимальная скорость (км/ч)
        self.brand = brand  # Марка автомобиля
        self.is_locked = True  # Заблокирована ли машина
        self.engine_running = False  # Запущен ли двигатель

    def info(self):
        """Вывод информации об автомобиле"""
        print(f"Марка: {self.brand}\nМасса: {self.mass} кг\nПробег: {self.km} км\n"
              f"Мощность: {self.power} л.с.\nМаксимальная скорость: {self.speed} км/ч\n"
              f"Заблокирована: {'Да' if self.is_locked else 'Нет'}\n"
              f"Двигатель работает: {'Да' if self.engine_running else 'Нет'}")

    def lock(self):
        """Блокировка машины"""
        self.is_locked = True
        print("Машина заблокирована.")

    def unlock(self):
        """Разблокировка машины"""
        self.is_locked = False
        print("Машина разблокирована.")

    def start_engine(self):
        """Запуск двигателя"""
        if not self.is_locked:
            self.engine_running = True
            print("Двигатель запущен.")
        else:
            print("Сначала разблокируйте машину!")

    def stop_engine(self):
        """Остановка двигателя"""
        if self.engine_running:
            self.engine_running = False
            print("Двигатель остановлен.")
        else:
            print("Двигатель уже выключен.")
