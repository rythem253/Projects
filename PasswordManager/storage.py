import sqlite3

conn = sqlite3.connect("database.db")

#Cursor is to send SQL commands
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vault ( 
        id INTEGER PRIMARY KEY,
        service TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )     
""")

cursor.execute("SELECT * FROM vault") 

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close