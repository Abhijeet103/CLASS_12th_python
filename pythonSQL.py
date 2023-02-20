# python sql
import mysql.connector

# database connection

db  =  mysql.connector.connect(
    host = 'localhost' ,
    user = 'root' ,
    password = 'Abhijeet@178' ,
    database  = 'mydb'

)

# db is my connector
# cursor

cursor = db.cursor()
# executing your sql statements

cursor.execute("select * from customers limit 5 offset 2")

result = cursor.fetchall()
#  fetchone  : only one data will be shown
# fetchall() :  gets all the data
# fetchmany(no of data)

# data when retrived is stored in your cursor
# for i in result:
#     print(i)
# for i in cursor:
#     print(i)

print(result)

sql = 'update customers set address = "Canyon 123" where address = "Valley 345"'
cursor.execute(sql)

cursor.execute("select * from customers")
result = cursor.fetchall()
#
# for i in result :
#     print(i)

# change is permanent  ?
# commit
db.commit()

sql =  'insert into customers (name , address) values ("Abhijeet" , "jaipur Rajasthan")'

cursor.execute(sql)

cursor.execute("select * from customers")
result = cursor.fetchall()
#
# for i in result :
#     print(i)

db.commit()

sql =  'insert into customers (name , address) values (%s , %s)'

val =  [('Akshat mathur' , 'mumbai') , ('Aditi' ,'jamshedpur')]

cursor.executemany(sql , val)

cursor.execute("select * from customers order by name")
result = cursor.fetchall()

for i in result :
    print(i)

db.commit()





