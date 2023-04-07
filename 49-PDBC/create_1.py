import mysql.connector


db = mysql.connector.connect(host='localhost',user='root',password='root')

C1 = db.cursor()

C1.execute('create database Meow')

print(C1)



#
# ('bird',)
# ('cat',)
# ('hospital',)
# ('information_schema',)
# ('meow',)
# ('mysql',)
# ('performance_schema',)
# ('saw',)
# ('sys',)