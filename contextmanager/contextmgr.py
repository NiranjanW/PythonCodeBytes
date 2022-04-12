import logging
import sqlite3
from contextlib import contextmanager


@contextmanager
def open_db(file_name: str):
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()

    try:
        yield cursor
    except sqlite3.DatabaseError as e:
        logging.error(e)
    finally:
        connection.close()


def main():
    logging.basicConfig(level=logging.INFO)
    with open_db(file_name="/Users/itnxw/database/application.db") as cursor:
        cursor.execute("SELECT * from blog")
        logging.info(cursor.fetchall())

if __name__ == "__main__":
    main()