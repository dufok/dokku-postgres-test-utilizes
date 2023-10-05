# dokku-postgres-test-utilizes

This is a simple python script to test the cpu utilization of a postgres database.

## Setup

`pip install -r requirements.txt`

## Usage

`python cpu_test_start.py -dsn=postgres://postgres:password@host:5432/namedb`

## Clean up

`python clean_database.py -dsn=postgres://postgres:password@host:5432/namedb`