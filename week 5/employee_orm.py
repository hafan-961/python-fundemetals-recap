from sqlalchemy.orm import declarative_base
from sqlalchemy import Column , Integer ,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#step 1
engine = create_engine("sqlite:///company.db")

#step 2
base = declarative_base()

#step 3
class Employee(base):
    __tablename__ = "employees"
    id = Column(Integer , primary_key = True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)

#Step 4
base.metadata.create_all(engine)

#step 5
Session = sessionmaker(bind = engine)
session = Session()
e1 = Employee(name = "Nobita" , age = 14 , department = "collector")
e2 = Employee(name = "dekesuki" , age = 15 , department ="peon")
# session.add(e1)
# session.add(e2)
session.commit()

# step6
# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id , i.name , i.age , i.department)

# step 7 update
# employees = session.query(Employee).filter_by(id = 1).first()
# employees.name = "Gian"
# session.commit()
# print("employee updated")
# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id , i.name , i.age , i.department)


# emp = session.query(Employee).filter(Employee.id == 1).first()
# if emp:
#     session.delete(emp)
#     session.commit()

# print("deleted")

# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id , i.name , i.age , i.department)


# stu = session.query(Employee).filter(Employee.age>18).all()
# session.commit()
# for i in stu:
#    session.delete(stu)
# session.commit()
# print('done')

# stu = session.query(Employee).all()
# for i in stu:
#     print(i.id , i.name , i.age , i.department)

#name is rahul and age is greater than 21
emp = session.query(Employee).filter(Employee.name == "rahul" , Employee.age>10).all()
# emp = session.query(Employee).filter(Employee.age > 18).one_or_none()
from sqlalchemy import desc , asc
emp = session.query(Employee).order_by(desc(Employee.id)).limit(2).all()
for i in emp:
    print(i.id , i.name , i.age , i.department)


'''
class Department(base):
    __tablename__ = "departments"
    id = Column(Integer , primary_key = True)
    name = Coulmn(String)
    students = relationship("student" , back_populates = "departments")

class student(base):
    __table__ = "students"
    id  = Column(Integer , primary_key = True)
    name = Column(String)
    age = Column(Integer)
    department_id = Column(Integer , ForeignKey("departments.id))
    department = relationship("Department" , back_populates = "students")







'''