import sqlite3

class DBConnection:

    def __init__(self, db_name=""):
        if db_name == "":
            print("CON_ERR : Please provide name for database to connect!")
            return
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":
    print("Non executable script")