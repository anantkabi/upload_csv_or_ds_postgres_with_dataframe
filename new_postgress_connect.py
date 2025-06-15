import psycopg2

# Define connection parameters
conn = psycopg2.connect(
    dbname="airflow",
    user="airflow",
    password="airflow",
    host="localhost",
    port="5432"  # Default PostgreSQL port
)

# Create a cursor object
cur = conn.cursor()

# Execute a test query
cur.execute("SELECT version();")

# Fetch and print results
print(cur.fetchone())

# Close the cursor and connection
cur.close()
conn.close()