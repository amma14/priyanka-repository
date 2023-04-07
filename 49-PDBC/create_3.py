import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='root',database='meow')


mydb=db.cursor()

data="Insert into sleep(sno, name, color, age) values (%s, %s,%s,%s)"
cat=[(5,'Tom','White',3)]

mydb.executemany(data,cat)
db.commit()