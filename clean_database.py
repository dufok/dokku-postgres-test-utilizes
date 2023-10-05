import psycopg2
import argparse

def clean_database(dsn):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(dsn)

    # Create a new database session and return a new instance of the Cursor class
    cur = conn.cursor()

    # Delete all rows from the table
    cur.execute("DELETE FROM test_table;")

    # Commit the changes
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Initialize argparse
    parser = argparse.ArgumentParser(description='Clean PostgreSQL database.')
    parser.add_argument('-dsn', type=str, help='Data Source Name for PostgreSQL', required=True)

    # Parse arguments
    args = parser.parse_args()

    # Run the function with the provided DSN
    clean_database(args.dsn)
