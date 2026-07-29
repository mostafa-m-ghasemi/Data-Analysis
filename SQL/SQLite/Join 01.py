import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT *
FROM Invoice
INNER JOIN Customer
ON Invoice.CustomerId = Customer.CustomerId
ORDER BY Customer.CustomerId
         """
         )
# Using of () is really important!!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()