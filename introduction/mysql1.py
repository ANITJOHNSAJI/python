import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="anit",
    password="pass123",
    database="Mydb1",
    
)
print("connection successfully")
connection.close()
