import psycopg2
import csv

# Параметры подключения к базе данных
conn_params = {
    "dbname": "phonebook_db",
    "user": "postgres",
    "password": "112430dar",
    "host": "localhost",
    "port": "5432"
}

def connect():
    try:
        conn = psycopg2.connect(**conn_params)
        return conn
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None

# 1. Вставка данных
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

# 2. Вставка данных консоль
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

# 3. Обновление
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

# 6. 
def search_by_pattern(pattern):
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
        rows = cur.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    except Exception as e:
        print(f"Ошибка поиска: {e}")
    finally:
        cur.close()
        conn.close()

# 7
def insert_or_update_user(first_name, phone):
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute("CALL insert_or_update_user(%s, %s)", (first_name, phone))
        conn.commit()
        print("Пользователь добавлен или обновлен")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cur.close()
        conn.close()

# 8
def insert_many_users(names, phones):
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute("CALL insert_many_users(%s, %s, NULL)", (names, phones))
        incorrect_data = cur.fetchone()[0]
        print("Результат:")
        for data in incorrect_data:
            print(data)
        conn.commit()
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cur.close()
        conn.close()

# 9
def get_paginated_data(limit, offset):
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_paginated_data(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cur.close()
        conn.close()

# 10
def delete_by_name_or_phone(value, delete_type):
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute("CALL delete_by_name_or_phone(%s, %s)", (value, delete_type))
        conn.commit()
        print("Данные удалены")
    except Exception as e:
        print(f"Ошибка: {e}")
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
        print("7. Поиск по шаблону")
        print("8. Добавить или обновить пользователя")
        print("9. Добавить несколько пользователей")
        print("10. Постраничный вывод данных")
        print("11. Удалить по имени или телефону")
        
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
        elif choice == "7":
            pattern = input("Введите шаблон для поиска: ")
            search_by_pattern(pattern)
        elif choice == "8":
            first_name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            insert_or_update_user(first_name, phone)
        elif choice == "9":
            names = input("Введите имена через запятую (например, John,Alice,Bob): ").split(",")
            phones = input("Введите телефоны через запятую (например, +1234567890,+0987654321,+5555555555): ").split(",")
            insert_many_users(names, phones)
        elif choice == "10":
            limit = int(input("Введите количество записей (limit): "))
            offset = int(input("Введите смещение (offset): "))
            get_paginated_data(limit, offset)
        elif choice == "11":
            delete_type = input("Удалить по (name/phone): ")
            value = input("Введите значение для удаления: ")
            delete_by_name_or_phone(value, delete_type)
        else:
            print("Неверный выбор")