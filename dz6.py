library_mvc/
│── model.py        # Модель (класс книги и интерфейс хранилища)
│── view.py         # Представление (отображение данных)
│── controller.py   # Контроллер (управление логикой)
│── main.py         # Точка входа в приложение


# model.py
from typing import List
from abc import ABC, abstractmethod

class Book:
    """Класс книги с основными атрибутами."""
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" ({self.year}) - {self.author}'

class IBookRepository(ABC):
    """Интерфейс хранилища книг (SOLID: Dependency Inversion)."""
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

class BookRepository(IBookRepository):
    """Реализация хранилища книг в памяти."""
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def get_all_books(self) -> List[Book]:
        return self.books


# view.py
from model import Book


class LibraryView:
    """Класс представления для работы с пользователем."""

    @staticmethod
    def show_books(books):
        """Вывод списка книг в консоль."""
        if not books:
            print("📚 Библиотека пуста!")
        else:
            print("\n📖 Список книг:")
            for book in books:
                print(f"  - {book}")

    @staticmethod
    def show_message(message):
        """Вывод информационного сообщения."""
        print(f"\nℹ️ {message}")

    @staticmethod
    def get_book_details():
        """Запрос данных у пользователя для добавления книги."""
        title = input("Введите название книги: ")
        author = input("Введите автора: ")
        year = int(input("Введите год издания: "))
        return Book(title, author, year)

    @staticmethod
    def get_book_title():
        """Запрос названия книги для удаления."""
        return input("Введите название книги для удаления: ")




# controller.py
from model import IBookRepository
from view import LibraryView

class LibraryController:
    """Контроллер для управления книгами."""

    def __init__(self, repository: IBookRepository, view: LibraryView):
        self.repository = repository
        self.view = view

    def add_book(self):
        """Добавление книги."""
        book = self.view.get_book_details()
        self.repository.add_book(book)
        self.view.show_message(f'✅ Книга "{book.title}" добавлена!')

    def remove_book(self):
        """Удаление книги."""
        title = self.view.get_book_title()
        self.repository.remove_book(title)
        self.view.show_message(f'❌ Книга "{title}" удалена!')

    def show_books(self):
        """Вывод всех книг."""
        books = self.repository.get_all_books()
        self.view.show_books(books)





# main.py
from model import BookRepository
from view import LibraryView
from controller import LibraryController

def main():
    """Главная функция приложения."""
    repository = BookRepository()
    view = LibraryView()
    controller = LibraryController(repository, view)

    while True:
        print("\n📚 Меню:")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            controller.show_books()
        elif choice == "2":
            controller.add_book()
        elif choice == "3":
            controller.remove_book()
        elif choice == "4":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный ввод!")

if __name__ == "__main__":
    main()
