import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "password123",
    database = "mydatabase"
)
mycursor = mydb.cursor()

# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)
'''ORDER BY ASC'''
# mycursor.execute("select * from customers order by name")
# myresult = mycursor.fetchall()
# for x in myresult: 
#     print(x)

'''Use the DESC keyword to sort the result in a descending order.'''
# mycursor.execute("select * from customers order by name desc")
# for x in mycursor:
#     print(x)
# mycursor.execute("insert into customers (name, address) values(%s, %s)", ("John_Doe", "Macao"))
# sql = "insert into customers (name, address) values(%s, %s)"
# vals = [
#     ("Quinn", "UK"),
#     ("Layla", "California"),
#     ("Goku", "Japan"),
#     ("Shin", "None"),
#     ('Amy', 'Apple st 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345')
# ]
# mycursor.executemany(sql, vals)

# mycursor.execute("delete from customers where address = 'Sri Lanka'")
# sql = "DELETE FROM customers WHERE address = 'UK'"

# mycursor.execute("delete from customers where address = 'Moscow'")
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# mydb.commit()
# print(mycursor.rowcount, "record(s) inserted")
'''DROP TABLE IF EXISTS'''
# sql = "DROP TABLE IF EXISTS employees"
# mycursor.execute(sql)
# mydb.commit()

    