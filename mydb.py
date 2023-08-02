import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

# cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mydb")

print("ALL DONE!")