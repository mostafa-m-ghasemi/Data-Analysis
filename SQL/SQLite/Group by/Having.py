import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT BillingCity, ROUND(AVG(total), 2)
FROM Invoice
GROUP BY BillingCity
HAVING avg(total) > 5
ORDER BY BillingCity
"""
         )
# Using of () is really important!!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()
