import sqlite3

# Connect to the database
conn = sqlite3.connect('application.db')

# Create a table
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert some data into the table
conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))
conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 30))
conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 35))

# Commit the changes
conn.commit()

# Read the data from the table
cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)

# Close the connection
conn.close()