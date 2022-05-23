# Connection of SQL with python
# !pip install mysql.connector-python

import mysql.connector as connection
try:
     mydb=connection.connect (host="localhost",user="root",passwd="mysql",use_pure=True)
     # check if the connection is established
     query="SHOW DATABASES"
     cursor=mydb.cursor() # create a cursor to execute quries
     cursor.execute(query)
     print(cursor.fetchall())
except Exception as e:
            mydb.close()
            print(str(e))

import mysql.connector as connection
connection.connect(host="localhost", users="root",passwd="mysql",use_pure=True)
conn=connection.connect(host="localhost",users="root",passwd="mysql",use_pure=True)
cur=conn.cursor()
conn.cursor()
cur.execute("show databases")
type(cur.execute("show databases"))
cur.fetchall()
res=cur.fetchall()
res
for i in res:
     print(i[0])
     

# Create New Datbase Python code
import mysql.connector as connection
conn=connection.connect(host="localhost",user="root",passwd="mysql",use_pure=True)
cur=conn.cursor()
cur.execute("create database Bhushan")
res=cur.fetchall()
res

import mysql.connector as connection
try:
     mydb=connection.connect(host="localhost",user="root",passwd="mysql",use_ppure=True)
     # check if the connection is established
     print(mydb.is_connected())
     query="Create database Student;"
     cursor=mydb.cursor() # create a cursor to execute queries
     cursor.execute(query)
     print("Database Created!")
     mydb.close()
except Exception as e:
       mydb.close()
       print(str(e))


# Create table 
import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database = 'sudhanshu12345',user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())

    query = "CREATE TABLE StudentDetails (Studentid INT(10) AUTO_INCREMENT PRIMARY KEY,FirstName VARCHAR(60)," \
            "LastName VARCHAR(60), RegistrationDate DATE,Class Varchar(20), Section Varchar(10))"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Table Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
    
    mydb.is_connected()
    cur=mydb.cursor()
    cur.execute("create table test(x1,INT(5), x2, VARCHAR(20),x3,DATE)")
    mydb.close()

# insert To Table
import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "INSERT INTO StudentDetails VALUES ('1132','Sachin','Kumar','1997-11-11','Eleventh','A')"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Values inserted into the table!!")
    mydb.commit()
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
