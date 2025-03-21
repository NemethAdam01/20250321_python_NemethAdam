from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='kiralyok')

cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)

cursor.execute("SELECT *  FROM uralkodo INNER JOIN hivatal ON uralkodo.azon = hivatal.azon WHERE uhaz_az = 1 ORDER BY hivatal.mettol ASC;")
for uralkodo in cursor:
    print(uralkodo)

cursor.execute("SELECT nev, COUNT(hivatal.azon) FROM hivatal INNER JOIN uralkodo on hivatal.uralkodo_az = uralkodo.azon GROUP BY uralkodo.nev HAVING COUNT(*) > 1;")
for uralkodo in cursor:
    print(uralkodo)

cursor.execute("""
    SELECT * FROM `uralkodo` 
    INNER JOIN hivatal ON uralkodo.azon = hivatal.azon
    ORDER BY ABS(hivatal.meddig - hivatal.mettol) DESC
    LIMIT 1""")
for uralkodo in cursor:
    print(uralkodo)
cnx.close()