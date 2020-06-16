#!/usr/bin/env python3

import psycopg2
import sys

IP = '192.168.0.100'
#IP = sys.argv[1]
PORT = 5432

USER = 'postgres'

PASSWORD = 'mem'
DATABASE = 'service'

conn = psycopg2.connect(host=IP, port=PORT, user=USER, password=PASSWORD, database=DATABASE)
cursor = conn.cursor()

query = (
    "SELECT table_name FROM information_schema.tables "
    "WHERE table_type = 'BASE TABLE' AND table_schema = 'public' "
    "ORDER BY table_type, table_name"
)
cursor.execute(query)

tables = cursor.fetchall()

print(tables)

for table, in tables:
    query = f'''SELECT * from {table}'''
    cursor.execute(query)
    rows = cursor.fetchmany(1000)
    while rows:
        print(rows, flush=True)
        rows = cursor.fetchmany(1000)
