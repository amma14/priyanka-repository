import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='meow')

mydb=db.cursor()

my='delete from sleep where age=2'
mydb.execute(my)

db.commit()