import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database = 'data',
    auth_plugin='mysql_native_password'
    )

mycursor = mydb.cursor()

exe = "SELECT * FROM test3"

mycursor.execute(exe)

res = mycursor.fetchall()

for x in res:
    print(x)