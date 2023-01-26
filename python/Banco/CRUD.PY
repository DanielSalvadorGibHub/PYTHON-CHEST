import mysql.connector

conex = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdmypy',

)

cursor = conex.cursor()



cursor.close()
conex.close()