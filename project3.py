# Re-import libraries after kernel reset
import sqlite3
import pandas as pd

# Connect to the uploaded Chinook database
conn = sqlite3.connect(r"C:\Users\Tahmid\Downloads\Chinook_Sqlite.sqlite")

# SQL query to fetch customer name, track name, and album title
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

# Run the query and store the result in a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Display the result
print (df)
