import logging
import sqlite3
import os
os.system("clear")

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Connection to database...")
    connection = sqlite3.connect("application.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        logging.info(cursor.fetchall())
    except sqlite3.DatabaseError as error:
        logging.error(error)
    finally:
        logging.info("Closing connection")
        connection.close()

if __name__ == "__main__":
    main()