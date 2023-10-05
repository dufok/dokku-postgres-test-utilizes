# dokku-postgres-test-utilizes

This is a simple python script to test the cpu utilization of a postgres database.

## Setup

`pip install -r requirements.txt`

inside cpu_test_start.py we have params:
# Number of threads to create
    num_threads = 5  
# Number of iterations for each thread
    total_iterations = 10000  

## Usage

`python cpu_test_start.py -dsn=postgres://postgres:password@host:5432/namedb`

## Clean up

`python clean_database.py -dsn=postgres://postgres:password@host:5432/namedb`