import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="Harlik*1", database = "youtubeAPI")
mycursor = mydb.cursor()


curr = mycursor

curr.execute("Select channelId from channelDesc")

records = curr.fetchall()

listRec = []
for i in records:
    listRec.append(i[0])
print(listRec)