import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT InvoiceDate,InvoiceId, CustomerId, Total 
            FROM Invoice
         WHERE DATE(InvoiceDate) = "2010-05-22" 
		 ORDER BY InvoiceDate """
         )
# when we using DATE function no need to write the time!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()