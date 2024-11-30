import sqlite3

# Path to your database
db_path = "../blog.db"

# Connect to the database
conn = sqlite3.connect(db_path)

# Create a cursor
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Query data from a specific table
cursor.execute("SELECT * FROM blogs;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()


# import os
# db_path = "../blog.db"
# print("Database absolute path:", os.path.abspath(db_path))
