import sqlite3


def connect_db():
    return sqlite3.connect("Northwind.db")


def show_products():
    """Выводит список товаров"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT ProductID, ProductName, UnitPrice FROM Products LIMIT 10")
    products = cursor.fetchall()
    conn.close()

    print("\nСписок товаров:")
    for product in products:
        print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}")


def add_customer():
    """Добавляет нового клиента в базу"""
    customer_id = input("Введите ID клиента (5 символов): ")
    company_name = input("Введите название компании: ")
    contact_name = input("Введите имя контактного лица: ")

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION;")
        cursor.execute("INSERT INTO Customers (CustomerID, CompanyName, ContactName) VALUES (?, ?, ?)",
                       (customer_id, company_name, contact_name))
        conn.commit()
        print("Клиент успешно добавлен!")
    except sqlite3.Error as e:
        conn.rollback()
        print("Ошибка при добавлении клиента:", e)
    finally:
        conn.close()


def main():
    while True:
        print("\n1. Показать список товаров")
        print("2. Добавить клиента")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            break
        else:
            print("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
