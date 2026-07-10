import sqlite3


class Database:
    def __init__(self, db_path="database.db"):
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

    def addStuff(self):
        self.cursor.execute("""
            INSERT INTO vault
            (service, username, password)
            VALUES (?,?,?)   
         """, ("google", "rythem", "112233"))
        
        self.conn.commit()

        
    def get_rows(self, query="Select * From vault"):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def deleteAll(self):
        self.cursor.execute("DELETE FROM vault")
        self.conn.commit()
    
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = Database()
    db.addStuff() 
    #db.deleteAll() #Remove if need to delete stuff from it
    rows = db.get_rows()
    print(rows)

    db.close()