import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT InvoiceId, CustomerId,BillingCity, Total 
            FROM Invoice
         WHERE BillingCity LIKE 'B%'"""  # ---> 'B%' ---> has 'B' at first, '%b%" --> has 'b' in the middle, '%b" --> has 'b' at the end
         )
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()