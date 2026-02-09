from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column , Integer ,String
from sqlalchemy.orm import sessionmaker

#step 1
engine = create_engine("sqlite:///school.db")  #sqlite is the database and school.db is file name
print("database created")
#step 2
base = declarative_base()
#base will be parent for all class

#step 3
class Student(base):
    __tablename__ = "students"
    id = Column(Integer , primary_key = True)
    name = Column(String)
    age = Column(Integer)
    course = Column(String)

base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()
s1 = Student(id = 1,name = "Rahul" , age = 20, course = "Python")
s2 = Student(id = 2,name = "Karan" , age = 21 ,course = "Java")
session.add(s1)
session.add(s2)
session.commit()
students = session.query(Student).all()
for i in students:
    print(i.id , i.name,i.age , i.course)


