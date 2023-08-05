import psycopg2

conn = psycopg2.connect(
    dbname = 'meukwid',
    user = 'postgres',
    password = '4456',
    host = 'localhost',
    port = '5432'
)