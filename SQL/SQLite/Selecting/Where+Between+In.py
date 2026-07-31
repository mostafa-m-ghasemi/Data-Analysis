import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT InvoiceId, CustomerId, Total 
            FROM Invoice
         WHERE Total BETWEEN 1.98 AND 5.0  """  # ---> total is between 1.98 and 5.0
         )
# WHERE IN(1.98, 3.96)  ---> total is 1.98 or 3.96
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()
