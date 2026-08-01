import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT c.LastName, c.FirstName, i.InvoiceId, i.CustomerId, i.InvoiceDate, i.total
FROM Invoice AS i
LEFT OUTER JOIN Customer AS c
ON i.CustomerId = c.CustomerId
ORDER BY c.CustomerId"""
         )
# Left outer join and right outer join!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()
