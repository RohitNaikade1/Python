import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="RN@gslab",
    database="data",
    auth_plugin='mysql_native_password'
)

mycursor=mydb.cursor()
mycursor.execute("show databases;")

data=mycursor.fetchall()

print(data)