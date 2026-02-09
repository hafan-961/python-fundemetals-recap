import sqlite3 as sq

#connect () create or open database
# connection1 = sq.connect("school.db")
# print("database connected")
# connection1.close()

# connection1 = sq.connect("school.db")
# #cursor() --> run sql
# cur = connection1.cursor()
# print("cursor created")
# connection1.close()

connection1 = sq.connect("school.db")
cur  = connection1.cursor()
cur.execute(""" CREATE TABLE students (id INTEGER , name TEXT ,marks INTEGER)""")
connection1.commit()
connection1.close()

# connection1 = sq.connect("school.db")
# cur = connection1.cursor()
# cur.execute("""INSERT INTO students VALUES (1, "AMIT" ,85) , (2,"NEHA" , 90)""")
# connection1.commit()
# connection1.close()

# connection1 = sq.connect("school.db")
# cur = connection1.cursor()
# cur.execute("select * from students")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# connection1.close()