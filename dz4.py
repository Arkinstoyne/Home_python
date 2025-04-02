import socket
import threading
import sqlite3
import datetime

HOST = '127.0.0.1'
PORT = 12345

# Настройка базы данных (SQLite)
conn_db = sqlite3.connect('messages.db', check_same_thread=False)
cursor = conn_db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message TEXT,
                    timestamp TEXT)''')
conn_db.commit()

def save_message(msg):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO messages (message, timestamp) VALUES (?, ?)", (msg, timestamp))
    conn_db.commit()

def client_handler(client_socket, addr):
    print(f"Подключился: {addr}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"От {addr}: {message}")
            save_message(f"{addr}: {message}")  # сохраняем сообщение в базу
            client_socket.sendall(data)  # отправляем эхо-ответ
        except Exception as e:
            print("Ошибка:", e)
            break
    client_socket.close()
    print(f"Отключился: {addr}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Сервер запущен и ожидает подключения...")
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=client_handler, args=(client_socket, addr), daemon=True).start()

if __name__ == '__main__':
    main()


#client

import socket

HOST = '127.0.0.1'
PORT = 12345

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Подключено к серверу. Для выхода введите 'exit'.")
    while True:
        message = input("Введите сообщение: ")
        if message.lower() == 'exit':
            break
        client.sendall(message.encode('utf-8'))
        data = client.recv(1024)
        print("Ответ от сервера:", data.decode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()
