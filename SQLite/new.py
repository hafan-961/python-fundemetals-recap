import sqlite3 as a 

# connection1 = a.connect("employees.db")
# cur = connection1.cursor()
# cur.execute("CREATE TABLE employees (id INTEGER , name TEXT , salary INTEGER)")
# print("tabel created")
# connection1.commit()
# connection1.close()

'appllied DML INSERT'
# connection1  = a.connect("employees.db")
# cur = connection1.cursor()
# cur.execute("INSERT INTO employees VALUES (1 , 'Hafan' , 60000) , (2 , 'elton' , 50000)")
# print("done")
# connection1.commit()
# connection1.close()

# connection1 = a.connect("employees.db")
# cur = connection1.cursor()
# cur.execute("SELECT * FROM employees")
# connection1.commit()
# connection1.close()

'applied DML SELECT'
# connection1 = a.connect("employees.db")
# cur = connection1.cursor()
# cur.execute("update employees set salary = 80000 where id = 1;")
# connection1.commit()
# cur.execute("SELECT * FROM employees")
# rows = cur.fetchall()
# for i in rows:
#     print(i)
# connection1.close()

'applied DML DELETE'
# connection1 = a.connect("employees.db")
# cur = connection1.cursor()
# cur.execute("delete FROM employees where id = 1;")
# connection1.commit()
# cur.execute("SELECT * FROM employees")
# rows = cur.fetchall()
# for i in rows:
#     print(i)
# connection1.close()

'applied DDL alter'
# connection1 = a.connect("employees.db")
# cur = connection1.cursor()
# cur.execute("ALTER table employees add hours INTEGER;")
# connection1.commit()
# cur.execute("SELECT * FROM employees")
# rows = cur.fetchall()
# for i in rows:
#     print(i)
# connection1.close()

'applying DML update'
# connection1 = a.connect("employees.db")
# cur = connection1.cursor()
# cur.execute("update employees set hours = 100 where id = 2;")
# connection1.commit()
# cur.execute("SELECT * FROM employees")
# rows = cur.fetchall()
# for i in rows:
#     print(i)
# connection1.close()

'applied DML insert' 

# connection1 = a.connect("employees.db")
# cur = connection1.cursor()
# cur.execute("INSERT INTO employees values(1, 'hafan' , 80000 , 90);")
# connection1.commit()
# cur.execute("SELECT * FROM employees")
# rows = cur.fetchall()
# for i in rows:
#     print(i)
# connection1.close()

'applied DDL TRUNCATE , and TCL begin taransaction'

connection1 = a.connect("employees.db")
cur = connection1.cursor()
cur.execute("BEGIN TRANSACTION;")
cur.execute("DELETE from employees;")
connection1.commit()
cur.execute("SELECT * FROM employees")
rows = cur.fetchall()
for i in rows:
    print(i)
connection1.close()