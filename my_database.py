import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", password = "mysql",
  user="root"
)

mycursor = mydb.cursor()

DATABASE = "mydatabase"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.execute(f"USE {DATABASE}")
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("ALTER TABLE customers ADD COLUMN  id INT AUTO_INCREMENT PRIMARY KEY")

sql = "INSERT IGNORE INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("új lekérdezés")
for x in myresult:
  print(x)