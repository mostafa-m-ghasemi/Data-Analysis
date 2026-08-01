import sqlite3

conn = sqlite3.connect("WSDA_Music.db")
cursor = conn.cursor()
query = ("""SELECT e.FirstName, e.LastName, e.EmployeeId, c.FirstName, c.LastName, c.SupportRepId, i.CustomerId, i.total
FROM Invoice AS i
INNER JOIN Customer AS c
ON i.CustomerId = c.CustomerId
INNER JOIN Employee AS e
ON c.SupportRepId = e.EmployeeId
ORDER BY total DESC
LIMIT 10"""
         )
# Left outer join and right outer join!!
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()
