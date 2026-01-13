import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = "root",
        password = "Igbunu@291997",
        database = "alx_book_store"
    )
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if mydb in locals() and mydb.is_connected():
        cursor.close()
        mydb.close()
    