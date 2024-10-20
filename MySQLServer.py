import mysql.connector

def createDB():
    try :
        conn = mysql.connector.connect(
            host = "localhost",
            user = "trinity985",
            password = "37022657",
            database = "alx_book_store"
        )

        miCursor = conn.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        if miCursor.execute(sql) :
            print("Database 'alx_book_store' created succesfully!")

        conn.commit()

    except Error as e :
        print("Did no connect. {e}")

    finally :
        if miCursor :
            miCursor.close()

        if conn :
            conn.close()
