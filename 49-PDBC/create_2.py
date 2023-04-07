import mysql.connector


db = mysql.connector.connect(host='localhost',user='root',password='root',database='meow')

C1 = db.cursor()

# C1.execute("create table sleep(sno int, name varchar(30), color varchar(30),age int)")
# C1.execute('show tables')
# for i in C1:
#     print(i)
# print(C1)

# ('sleep',)
