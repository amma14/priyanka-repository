import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='root',database='meow')

mydb = db.cursor()


mydb1='update sleep set name="Tomy" where  color="black"'
mydb.execute(mydb1)
db.commit()