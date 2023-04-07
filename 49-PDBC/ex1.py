import mysql.connector

import mysql.connector

x = mysql.connector.connect(user='root',host='localhost',password='root')
print(x)
if x:
    print('connected mysql')

else:
    print('disconnected mysql')


# <mysql.connector.connection_cext.CMySQLConnection object at 0x00000207A5CE8DC0>
# connected mysql
