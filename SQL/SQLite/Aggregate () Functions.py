import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT SUM(total) AS [Toyal Sales], AVG(total) AS [Avrage Sales], MAX(total) AS [Maximun Sales],
MIN(total) AS [Minumum Sales], COUNT(total) AS [Total count of Sales]
FROM Invoice
"""
         )
# Using of () is really important!!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()