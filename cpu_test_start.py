import psycopg2
import argparse
from random import randint
from tqdm import tqdm  # <-- New import for the status bar

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate CPU load on a PostgreSQL database.')
parser.add_argument('-dsn', '--data_source_name', type=str, required=True, help='The Data Source Name (DSN) for connecting to PostgreSQL.')
args = parser.parse_args()

print("Attempting to connect to the database...")
try:
    # Connect to PostgreSQL database using the provided DSN
    conn = psycopg2.connect(args.data_source_name)
    print("Successfully connected to the database.")
except Exception as e:
    print(f"Failed to connect to the database: {e}")
    exit(1)

# Create a table
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test_table (id serial PRIMARY KEY, num integer);")
conn.commit()
print("Table 'test_table' created or already exists.")

# Insert random data into the table in a loop to generate load
print("Starting to insert data and run queries...")
for i in tqdm(range(1000)):  # <-- Using tqdm for the status bar, running 1000 iterations
    random_num = randint(0, 1000)
    cur.execute("INSERT INTO test_table (num) VALUES (%s);", (random_num,))
    conn.commit()

    # Run a CPU-intensive query
    cur.execute("SELECT num, COUNT(*) FROM test_table GROUP BY num ORDER BY COUNT(*) DESC;")
    rows = cur.fetchall()

print("Completed 1000 iterations.")

# Close the cursor and the connection
cur.close()
conn.close()
print("Cursor and connection closed.")
