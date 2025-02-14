# init_db.py
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('airlinez_test.db')
cursor = conn.cursor()

# Read and execute the schema.sql file
with open('schema.sql', 'r') as f:
    cursor.executescript(f.read())

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database initialized successfully!")