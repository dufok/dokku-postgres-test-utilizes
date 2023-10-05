import psycopg2
import argparse
import threading
from random import randint
from tqdm import tqdm

def run_queries(dsn):
    try:
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test_table (id serial PRIMARY KEY, num integer);")
        cur.execute("CREATE TABLE IF NOT EXISTS another_table (id serial PRIMARY KEY, value integer);")
        conn.commit()

        for i in tqdm(range(1000)):
            random_num = randint(0, 1000)
            cur.execute("INSERT INTO test_table (num) VALUES (%s);", (random_num,))
            cur.execute("INSERT INTO another_table (value) VALUES (%s);", (random_num,))
            conn.commit()

            cur.execute("""
            SELECT t1.num, t2.value, COUNT(*)
            FROM test_table t1
            JOIN another_table t2 ON t1.id = t2.id
            GROUP BY t1.num, t2.value
            ORDER BY COUNT(*) DESC;
            """)
            rows = cur.fetchall()
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Thread failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate CPU load on a PostgreSQL database.')
    parser.add_argument('-dsn', '--data_source_name', type=str, required=True, help='The Data Source Name (DSN) for connecting to PostgreSQL.')
    args = parser.parse_args()

    num_threads = 5  # Number of threads to create

    print(f"Starting {num_threads} threads to connect to the database and run queries.")

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=run_queries, args=(args.data_source_name,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("All threads completed.")

