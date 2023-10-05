import psycopg2
import argparse
from random import randint

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate CPU load on a PostgreSQL database.')
parser.add_argument('-dsn', '--data_source_name', type=str, required=True, help='The Data Source Name (DSN) for connecting to PostgreSQL.')
args = parser.parse_args()

# Connect to PostgreSQL database using the provided DSN
conn = psycopg2.connect(args.data_source_name)

# Create a table
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test_table (id serial PRIMARY KEY, num integer);")
conn.commit()

# Insert random data into the table in a loop to generate load
while True:
    random_num = randint(0, 1000)
    cur.execute("INSERT INTO test_table (num) VALUES (%s);", (random_num,))
    conn.commit()

    # Run a CPU-intensive query
    cur.execute("SELECT num, COUNT(*) FROM test_table GROUP BY num ORDER BY COUNT(*) DESC;")
    rows = cur.fetchall()

# Close the cursor and the connection (though this part won't be reached in an infinite loop)
cur.close()
conn.close()
