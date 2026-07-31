import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT InvoiceDate,InvoiceId, CustomerId, Total, BillingCity 
            FROM Invoice
         WHERE total > 1.98 AND (BillingCity LIKE "P%" OR BillingCity LIKE "D%") 
		 ORDER BY InvoiceDate  """
         )
# Using of () is really important!!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()
