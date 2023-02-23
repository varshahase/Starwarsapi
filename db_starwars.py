"""
user: root
password: qwerty
host: 127.0.0.1
port: 3306
database: starwarsDB
"""

import pyMySQL.cursors

# Connect to the database
connection = pyMySQL.connect(host='127.0.0.1',
                             user='root',
                             port=3306,
                             password='Varsha@1995',
                             database='starwarsDB',
                             cursorclass=pyMySQL.cursors.DictCursor)
cursor=connection.cursor()
cursor.execute("SHOW DATABASES")
results=cursor.fetchall()
for result in results:
    print (result)