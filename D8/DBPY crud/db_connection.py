import mysql.connector 
from mysql.connector import Error
def connect_db():
    """Establish a connection to the MySQL database."""
    try:
        connection=mysql.connector.connect(
            host ='localhost',
            database='empmanagement',
            user='root',
            password='mysql@123',
            
        )
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL:{e}")
        return None 