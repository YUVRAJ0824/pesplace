import os
from db_connection import connect_db
try:
    conn = connect_db()
    if conn.is_connected():
        print("Connection to the database was successful!")
    conn.close()
except Exception as e:
    print(f"An error ocurred:{e}")