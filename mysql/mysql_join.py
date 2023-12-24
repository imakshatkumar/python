import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost", 
    username = "root", 
    password = "password123",
    database = "mydatabase"
)
'''ALA we only need to view/show stuff, we don't need to use teh .commit() function
that is only used when any kind of changes are made...'''
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(24), origin VARCHAR (34))")
# sql = "insert into products (name, origin) values(%s, %s)"
# val = [
#     ("Demons", "Red Hell"),
#     ("Angels", "Heaven"), 
#     ("Elves", "Forest"), 
#     ("Dwarfs", "the underground city")
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
mycursor.execute("select * from products")
myresult = mycursor.fetchall()
for x in myresult: 
    print(x)
sql = "SELECT \
    customers.name AS customer, \
    products.name AS favorite \
    FROM customers \
    INNER JOIN products ON customers.name = products."
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult: 
    print(x)

