import unittest
import requests
from unittest.mock import patch


# Функция для вычисления факториала
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Функция для сортировки списка
def sort_list(numbers):
    return sorted(numbers)


# Функция для получения погоды
def get_weather(city):
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Тесты для функций
class TestFunctions(unittest.TestCase):

    # Тесты для функции factorial
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_large(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(RecursionError):  # factorial не определен для отрицательных чисел
            factorial(-1)

    # Тесты для функции sort_list
    def test_sort_integers(self):
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])

    def test_sort_floats(self):
        self.assertEqual(sort_list([1.5, 3.2, 2.1]), [1.5, 2.1, 3.2])

    def test_sort_mixed(self):
        self.assertEqual(sort_list([3, 2.5, 1]), [1, 2.5, 3])

    def test_sort_empty(self):
        self.assertEqual(sort_list([]), [])

    # Тесты для функции get_weather
    @patch('requests.get')
    def test_get_weather_valid(self, mock_get):
        # Мокаем успешный ответ
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"current": {"temp_c": 20, "condition": {"text": "Clear"}}}

        city = "London"
        result = get_weather(city)
        self.assertEqual(result["current"]["temp_c"], 20)
        self.assertEqual(result["current"]["condition"]["text"], "Clear")

    @patch('requests.get')
    def test_get_weather_invalid_city(self, mock_get):
        # Мокаем неуспешный ответ
        mock_get.return_value.status_code = 404

        city = "UnknownCity"
        result = get_weather(city)
        self.assertIsNone(result)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()

