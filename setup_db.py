import sqlite3

connect = sqlite3.connect("books.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    pages INTEGER,
    status TEXT
)'''
)

connect.commit()
connect.close()
print("veri tabanı başarıyla oluşturuldu")


