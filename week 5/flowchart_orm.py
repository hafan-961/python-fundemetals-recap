connect_enigne()
declarative_base()
create table (using session)
create table2 (using session)
commit
base metadata create_all(engine)
insertion of data 
    session = sessionmaker(bind = engine)
    session = session()

-> session.add(s1)
-> session.add(s2)
-> commit()
-> emp = session(Employee).all()
-> UPDATE
-> DELETE

