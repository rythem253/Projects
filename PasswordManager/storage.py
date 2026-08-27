import sqlite3
import os

# Same fix as main.py: resolve the db file relative to this script's
# folder, not whatever directory the app happens to be launched from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB_PATH = os.path.join(BASE_DIR, "database.db")


class Database:
    def __init__(self, db_path=DEFAULT_DB_PATH):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vault ( 
                id INTEGER PRIMARY KEY,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
                )     
        """)

        self.conn.commit()

    def addStuff(self, service, username, password):
        self.cursor.execute("""
            INSERT INTO vault
            (service, username, password)
            VALUES (?,?,?)   
        """, (service, username, password))
        
        self.conn.commit()

        
    def get_rows(self, query="Select * From vault"):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def deleteAll(self):
        self.cursor.execute("DELETE FROM vault")
        self.conn.commit()
    
    def close(self):
        self.conn.close()

    # def displayAll(self, query="Select password From vault"):
    #     self.cursor.execute(query)
    #     self.conn.commit()
    #     print(query)



if __name__ == "__main__":
    db = Database()
    db.addStuff() 
    #db.deleteAll() #Remove if need to delete stuff from it
    rows = db.get_rows()
    print(rows)

    db.close()