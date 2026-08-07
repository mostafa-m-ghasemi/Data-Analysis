import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT BillingCountry,BillingCity, ROUND(AVG(total), 2)
FROM Invoice
GROUP BY BillingCountry, BillingCity
HAVING avg(total) > 5
ORDER BY BillingCountry
"""
         )
# Using of () is really important!!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()