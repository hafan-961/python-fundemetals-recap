import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",      # fixed (instead of localhost)
    database="school",     # comma added
    user="postgres",
    password="root",       # must be your REAL postgres password
    port="5432"
)

print("Connected successfully")

