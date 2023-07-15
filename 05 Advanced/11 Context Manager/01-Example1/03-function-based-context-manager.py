import logging
import sqlite3
import os
from contextlib import contextmanager
os.system("clear")

@contextmanager
def open_sqlite(db_name: str):
    logging.info("Connection to database...")
    connection = sqlite3.connect(db_name)
    try:
        cursor = connection.cursor()
        yield cursor
    except sqlite3.DatabaseError as error:
        logging.error(error)
    finally:
        logging.info("Closing connection")
        connection.close()
    

def main():
    logging.basicConfig(level=logging.INFO)
    with open_sqlite("application.db") as cursor:
        cursor.execute("SELECT * FROM users")
        logging.info(cursor.fetchall())

if __name__ == "__main__":
    main()