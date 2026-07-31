import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT FirstName, LastName, Address,
FirstName ||' '|| LastName ||' '|| Address ||',' || City || ',' || State || ' ' || PostalCode AS [Mailling addres]
FROM Customer
where Country = 'USA'"""
         )
# Using of () is really important!!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()