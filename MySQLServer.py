import mysql.connector

conn = mysqli.connector.connect(
    host = "localhost",
    user = "trinity985",
    password = "37022657",
    database = "alx_book_store"
)

def createDB():
    miCursor = conn.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"

    if miCursor.execute(sql) :
        print("Database 'alx_book_store' created succesfully!")

    conn.commit()
