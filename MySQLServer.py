import mysql.connector
from mysql.connector import Error

def createDB():
    conn = None
    miCursor = None
    try :
        conn = mysql.connector.connect(
            host = "localhost",
            user = "trinity985",
            password = "37022657"
        )

        if conn.is_connected() :
            miCursor = conn.cursor()
            sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            miCursor.execute(sql) :
            print("Database 'alx_book_store' created succesfully!")

            conn.commit()

    except mysql.connector.Error as e :
        print(f"Error: {e}")

    except Error as e :
        print("Did no connect. {e}")

    finally :
        if miCursor :
            miCursor.close()

        if conn :
            conn.close()

createDB()
