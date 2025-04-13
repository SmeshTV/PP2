import psycopg2
import csv

# подключения к базе данных
conn_params = {
    "dbname": "phonebook_db",
    "user": "postgres",
    "password": "112430dar",
    "host": "localhost",
    "port": "5432"
}

def connect():
    """Подключение к базе данных"""
    try:
        conn = psycopg2.connect(**conn_params)
        return conn
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None

# 1. Вставка данных из CSV
def insert_from_csv(file_path):
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
        conn.commit()
        print("Данные из CSV успешно загружены")
    except Exception as e:
        print(f"Ошибка при загрузке из CSV: {e}")
    finally:
        cur.close()
        conn.close()

# 2. Вставляем данных с консоли
def insert_from_console():
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        first_name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        cur.execute(
            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
            (first_name, phone)
        )
        conn.commit()
        print("Данные успешно добавлены")
    except Exception as e:
        print(f"Ошибка при добавлении: {e}")
    finally:
        cur.close()
        conn.close()

# 3. Обновление данных
def update_data():
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        print("Выберите, что обновить: 1 - имя, 2 - телефон")
        choice = input("Ваш выбор: ")
        username = input("Введите имя пользователя для обновления: ")
        
        if choice == "1":
            new_name = input("Введите новое имя: ")
            cur.execute(
                "UPDATE phonebook SET first_name = %s WHERE first_name = %s",
                (new_name, username)
            )
        elif choice == "2":
            new_phone = input("Введите новый телефон: ")
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE first_name = %s",
                (new_phone, username)
            )
        else:
            print("Неверный выбор")
            return
        
        conn.commit()
        print("Данные успешно обновлены")
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")
    finally:
        cur.close()
        conn.close()

# 4. Запрос данных с фильтрами
def query_data():
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        print("Выберите фильтр: 1 - по имени, 2 - по телефону, 3 - все записи")
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            name = input("Введите имя для поиска: ")
            cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{name}%",))
        elif choice == "2":
            phone = input("Введите телефон для поиска: ")
            cur.execute("SELECT * FROM phonebook WHERE phone ILIKE %s", (f"%{phone}%",))
        elif choice == "3":
            cur.execute("SELECT * FROM phonebook")
        else:
            print("Неверный выбор")
            return
        
        rows = cur.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    except Exception as e:
        print(f"Ошибка при запросе: {e}")
    finally:
        cur.close()
        conn.close()

# 5. Удаление данных
def delete_data():
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        print("Удалить по: 1 - имени, 2 - телефону")
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            name = input("Введите имя для удаления: ")
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        elif choice == "2":
            phone = input("Введите телефон для удаления: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        else:
            print("Неверный выбор")
            return
        
        conn.commit()
        print("Данные успешно удалены")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    while True:
        print("\nPhoneBook Menu:")
        print("1. Загрузить данные из CSV")
        print("2. Добавить данные с консоли")
        print("3. Обновить данные")
        print("4. Запросить данные")
        print("5. Удалить данные")
        print("6. Выход")
        
        choice = input("Выберите действие: ")
        if choice == "1":
            insert_from_csv("phonebook.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            break
        else:
            print("Неверный выбор")