import mysql.connector

mydb = mysql.connector.connect(
  name="telkom",
  host="localhost",
  user="root",
  password="",
  port="3306"
)

print(mydb)