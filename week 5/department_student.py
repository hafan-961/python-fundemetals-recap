from sqlalchemy.orm import declarative_base , relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer , Column , String , ForeignKey 
from sqlalchemy import create_engine

engine = create_engine("sqlite:///google.db")
print("database created")

base = declarative_base()

class Department(base):
    __tablename__ = "departments"
    id = Column(Integer , primary_key = True)
    name = Column(String)
    students = relationship("students" , back_populates = "departments")

class student(base):
    __tablename__ = "students"
    id  = Column(Integer , primary_key = True)
    name = Column(String)
    age = Column(Integer)
    department_id = Column(Integer , ForeignKey("departments.id"))
    department = relationship("Department" , back_populates = "students")

base.metadata.create_all(engine)

