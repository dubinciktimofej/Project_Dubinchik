import sqlite3
import books

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Создание таблицы, очистка и загрузка книг из books.py
cur.execute("""CREATE TABLE IF NOT EXISTS Каталог (
    Код_книги INTEGER PRIMARY KEY AUTOINCREMENT,
    Жанр TEXT, Страна TEXT, Серия TEXT, Автор TEXT,
    Название TEXT, Год INTEGER, Аннотация TEXT)""")
cur.execute("DELETE FROM Каталог")
cur.execute("DELETE FROM sqlite_sequence WHERE name='Каталог'")
cur.executemany("""INSERT INTO Каталог
    (Жанр, Страна, Серия, Автор, Название, Год, Аннотация)
    VALUES (?, ?, ?, ?, ?, ?, ?)""", books.BOOKS)
conn.commit()

def show():
    for row in cur.execute("SELECT * FROM Каталог").fetchall():
        print(row)

def find():
    # 3 критерия поиска: автор, жанр, год
    print("1-Автор  2-Жанр  3-Год")
    c, v = input("Критерий: "), input("Значение: ")
    try:
        queries = {
            "1": ("SELECT * FROM Каталог WHERE Автор LIKE ?", (f"%{v}%",)),
            "2": ("SELECT * FROM Каталог WHERE Жанр = ?", (v,)),
            "3": ("SELECT * FROM Каталог WHERE Год = ?", (int(v),)),
        }
        if c not in queries:
            return print("Неверный критерий.")
        result = cur.execute(*queries[c]).fetchall()
        [print(r) for r in result] if result else print("Не найдено.")
    except ValueError:
        print("Ошибка: год должен быть числом.")

def delete():
    # 3 критерия удаления: код, название, год
    print("1-Код  2-Название  3-Год")
    c, v = input("Критерий: "), input("Значение: ")
    try:
        queries = {
            "1": ("DELETE FROM Каталог WHERE Код_книги = ?", (int(v),)),
            "2": ("DELETE FROM Каталог WHERE Название LIKE ?", (f"%{v}%",)),
            "3": ("DELETE FROM Каталог WHERE Год = ?", (int(v),)),
        }
        if c not in queries:
            return print("Неверный критерий.")
        cur.execute(*queries[c])
        conn.commit()
        print(f"Удалено: {cur.rowcount}")
    except ValueError:
        print("Ошибка: код и год должны быть числами.")

def edit():
    # Находим книгу по коду, затем меняем одно из трёх полей
    try:
        code = int(input("Код книги: "))
        book = cur.execute(
            "SELECT * FROM Каталог WHERE Код_книги = ?", (code,)
        ).fetchone()
        if not book:
            return print("Не найдена.")
        print(book)
        print("1-Автор  2-Название  3-Год")
        fields = {"1": "Автор", "2": "Название", "3": "Год"}
        f = input("Что изменить: ")
        if f not in fields:
            return print("Неверный критерий.")
        cur.execute(
            f"UPDATE Каталог SET {fields[f]} = ? WHERE Код_книги = ?",
            (input("Новое значение: "), code)
        )
        conn.commit()
        print("Обновлено.")
    except ValueError:
        print("Ошибка: код должен быть числом.")

while True:
    print("\n1-Показать  2-Найти  3-Удалить  4-Редактировать  0-Выход")
    choice = input("Выбор: ")
    if   choice == "1": show()
    elif choice == "2": find()
    elif choice == "3": delete()
    elif choice == "4": edit()
    elif choice == "0": break

conn.close()