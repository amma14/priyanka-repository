import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='meow')

mydb=db.cursor()
# mydb.execute("select * from sleep")
# (1, 'cat1', 'white', 1)
# (2, 'cat2', 'black', 3)
# (3, 'cat3', 'blue', 4)
# (4, 'cat4', 'black&white', 2)
# (5, 'Tom', 'White', 3)


mydb.execute('select * from sleep limit 3')
# output=mydb.fetchone()
for i in mydb:
    print(i)
# (1, 'cat1', 'white', 1)
# (2, 'cat2', 'black', 3)
# (3, 'cat3', 'blue', 4)


