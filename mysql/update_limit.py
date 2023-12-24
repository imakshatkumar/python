import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    username = "root", 
    password = "password123",
    database = "mydatabase"
)
"LIMIT: used to limit the result"
mycursor = mydb.cursor()
# mycursor.execute("select * from customers order by name desc LIMIT 5")
# myresult = mycursor.fetchall()
# for x in myresult: 
#     print(x)
# sql = "insert into customers (name, address) values (%s, %s)"
# val = [
#     ("Ray", "Dragon_City"),
#     ("Novice", "Zom100"), 
#     ("Quinn", "NightTale")
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# myresult = mycursor.fetchall()
# for x in myresult: 
#     print(x)
'''UPDATE: You can update records in a table using the update function...'''
# sql = "update customers set address = 'Blade Island' where address = 'Apple st 652'"
    
# mycursor.execute(sql)
# mydb.commit()
'''
Prevent SQL Injection
It is considered a good practice to escape the values of any query, also in update statements.
This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
The mysql.connector module uses the placeholder %s to escape values in the delete statement:
'''
# sql = "update customers set address = %s where address = %s"
# val = ("Heaven", "Valley 345")
# mycursor.execute(sql, val)
# mydb.commit()
'''If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:'''
# mycursor.execute("select * from customers order by name desc LIMIT 5 offset 3")
# myresult = mycursor.fetchall()
# for x in myresult: 
#     print(x)
