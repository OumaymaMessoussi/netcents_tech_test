import psycopg2

from global_variables import DB_NAME, PASSWORD, PORT, USERNAME

# Replace with your PostgreSQL credentials and database information
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/template1"

# Connect to the PostgreSQL database
connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# Execute a SELECT query to fetch all rows from the table
cursor.execute("SELECT * FROM unconfirmed_transactions")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the content of the table
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
