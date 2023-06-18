import os
import sqlite3

conn = sqlite3.connect('data/database.db')

def check_db_file_exists(conn):
    if os.path.isfile(conn):
        print(f"The database file '{conn}' exists.")
    else:
        print(f"The database file '{conn}' does not exist.")

# Example usage
database_file = "./data/database.db"
check_db_file_exists(database_file)