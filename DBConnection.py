import mysql.connector
from mysql.connector import Error

class Db:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="ev_db",
                port=3306
            )
            self.cur = self.cnx.cursor(dictionary=True, buffered=True)
            print("Database connection successful!")
        except Error as e:
            print(f"Error connecting to the database: {e}")
            self.cnx = None
            self.cur = None

    def select(self, q, params=None):
        try:
            self.cur.execute(q, params)
            return self.cur.fetchall()
        except Error as e:
            print(f"Error executing SELECT query: {e}")
            return None

    def selectOne(self, q, params=None):
        try:
            self.cur.execute(q, params)
            return self.cur.fetchone()
        except Error as e:
            print(f"Error executing SELECT ONE query: {e}")
            return None

    def insert(self, q, params=None):
        try:
            self.cur.execute(q, params)
            self.cnx.commit()
            return self.cur.lastrowid
        except Error as e:
            print(f"Error executing INSERT query: {e}")
            return None

    def update(self, q, params=None):
        try:
            self.cur.execute(q, params)
            self.cnx.commit()
            return self.cur.rowcount
        except Error as e:
            print(f"Error executing UPDATE query: {e}")
            return None

    def delete(self, q, params=None):
        try:
            self.cur.execute(q, params)
            self.cnx.commit()
            return self.cur.rowcount
        except Error as e:
            print(f"Error executing DELETE query: {e}")
            return None

    def __del__(self):
        if self.cur:
            self.cur.close()
        if self.cnx:
            self.cnx.close()
        print("Database connection closed.")
