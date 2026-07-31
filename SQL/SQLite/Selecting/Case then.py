import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT InvoiceDate, BillingAddress, BillingCity, total,
CASE 
WHEN total < 2.00 THEN 'Baseline Purchase'
WHEN total BETWEEN 2.00 AND 6.99 THEN 'Low Purchase'
WHEN total BETWEEN 7.00 AND 15.00 THEN 'Target Purchase'
ELSE 'Top Perfoemer'
END AS 'Purchase Type'
FROM Invoice
ORDER BY InvoiceDate 
         """
         )
# Using of () is really important!!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()
