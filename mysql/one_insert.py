'''MySQL''' # It's not case-sensitive...
import mysql.connector
# # 412_B : 10-11
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
    database = "mydatabase"
)

print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE ANIME")     # already created

# mycursor.execute("SHOW DATABASES")

# # prints the databases in mycursor: 
# for x in mycursor: 
#     print(x)

# # TO CREATE A TABLE
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
'''
When creating a table, you should also create a column with a unique key for each record.
This can be done by defining a PRIMARY KEY.
We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. 
Starting at 1, and increased by one for each record
'''
# mycursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(24))")
# mycursor.execute("ALTER TABLE customers add column id int auto_increment primary key")

sql1 = "insert into customers (name, address) values (%s, %s)"
val1 = ("John", "Highway_21")

sql2 = "insert into customers (name, address) values (%s, %s)"
val2 = ("Kushagra", "GP Road")

mycursor.execute(sql1, val1)
mycursor.execute(sql2, val2)    # will not work as this method can only add one value

'''INSERT'''
# use executemany function, to add many entries: 
# sql3 = "insert into customers (name, address) values (%s, %s)"
# val3 = [
#     ("Eva", "Moscow"),
#     ("Raily", "California"),
#     ("Johnny", "UK"),
#     ("Lily", "Sri Lanka"),
#     ("Kush", "Bihar"),
#     ("Freya", "Peterson")
# ]

# mycursor.executemany(sql3, val3)
# mycursor.execute("select * from customers")

# myresult = mycursor.fetchall()
myresult = mycursor.fetchone()

print(myresult)

mycursor.execute("select name, address from customers")

# mydb.commit()

# print(mycursor.rowcount, "Record Inserted")
# print("last recorded ID: ", mycursor.lastrowid)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mydb.commit()
'''
Important!: the statement: mydb.commit(). 
is required to make the changes, otherwise no changes are made to the table.
'''


