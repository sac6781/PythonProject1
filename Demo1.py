import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='root',auth_plugin='caching_sha2_password',database='db1')
mycursor=mydb.cursor()
mycursor.execute("insert into sach values('Sachin',21213,'As Lpu 2')")
mycursor.execute("select * from sach")
for i in mycursor:
    print(i)

print("Let's print the findings after the Where Clause")

mycursor.execute("select * from sach where name1 in('Sachin','Singh') and id<5000 ")
result=mycursor.fetchall()
for j in result:
    print(j)

print("Print name values where id is in between 3000 to 100000")
mycursor.execute("Select name1 from sach where id>3000 ")
result2=mycursor.fetchall()
for k in result2:
    print(k)