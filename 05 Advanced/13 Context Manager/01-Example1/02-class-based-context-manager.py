import logging
import sqlite3
import os
os.system("clear")

class OpenSQLite:
    def __init__(self, db_name: str):
        logging.info("Connection to database...")
        self.conn = sqlite3.connect(db_name)

    def __enter__(self):
        logging.info("Calling __enter__...")
        return self.conn.cursor()

    # def __exit__(self, *args):
    def __exit__(self, exception_type, exception_value, traceback):
        if exception_value:
            logging.error(exception_value)
        self.conn.commit()
        logging.info("Calling __exit__...")
        self.conn.close()


def main():
    logging.basicConfig(level=logging.INFO)
    with OpenSQLite("application.db") as cursor:
        cursor.execute("SELECT * FROM users")
        logging.info(cursor.fetchall())

if __name__ == "__main__":
    main()