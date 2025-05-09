
import sqlite3
import pandas as pd


conn = sqlite3.connect(r"C:\Users\Tahmid\Downloads\Chinook_Sqlite.sqlite")


query = """
SELECT 
    c.LastName, 
    c.FirstName, 
    t.Name AS TrackName, 
    al.Title AS AlbumTitle
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album al ON t.AlbumId = al.AlbumId
ORDER BY c.LastName, c.FirstName
LIMIT 5;
"""


df = pd.read_sql_query(query, conn)


conn.close()


print (df)
