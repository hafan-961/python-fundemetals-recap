import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    database = "store_db",
    user = "postgres",
    password = "root"
)
print("Connected")
cur = conn.cursor()
cur.execute("""create table employees (id int, name varchar(50),salary int )""")
conn.commit()
cur.execute("""insert into employees values(2,'shan',22) """)
conn.commit()
cur.execute("""select * from employees""")
rows=cur.fetchall()
for i in rows:
    print(i)
conn.close()