import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "password123", 
    database = "mydatabase"
)

print(mydb)

mycursor = mydb.cursor()
'''SELECT FROM A TABLE'''
# mycursor.execute("select * from customers")
# myresult = mycursor.fetchall()
# for x in myresult: 
#     print(x)
'''Selecting columns'''
# mycursor.execute("select name, address from customers")
# myresult = mycursor.fetchall()
# for x in myresult: 
#     print(x)
'''Using the fetchone() methods to get only ONE row [First]'''
# mycursor.execute("select * from customers")
# myresult = mycursor.fetchone()
# print(myresult)
'''SELECT WITH A FILTER'''
# sql = "select * from customers where address  = 'Bihar'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# for x in myresult: 
#     print(x)

'''Wildcard Characters
You can also select the records that starts, includes, or ends with a given letter or phrase.
Use the %  to represent wildcard characters:'''
# mycursor.execute("select * from customers where address like '%way%'")
# myresult = mycursor.fetchall()
# for x in myresult: 
#     print(x)
'''
Prevent SQL Injection
When query values are provided by the user, you should escape the values.
This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
The mysql.connector module has methods to escape query values:
'''     # Escape query values by using the placholder %s method
sql1 = "select * from customers where address = %s"
adr = ("Highway_21", )
mycursor.execute(sql1, adr)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mydb.commit()


