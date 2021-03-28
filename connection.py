import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1", user="<UserName>", password="<Password>")
mycursor = mydb.cursor()
