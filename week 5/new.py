from sqlalchemy import create_engine , Integer , String ,Column , ForeignKey
from sqlalchemy.orm import sessionmaker , declarative_base , relationship

engine  = create_engine("sqlite:///hafan.db")
base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class HAFAN(base):
    __tablename__ = "hafan"
    id = Column(Integer , primary_key = True)
    name = Column(String , ForeignKey("parents.name"))
    cates = relationship("parent" , "category")

class parent(base):
    __tablename__ = "parents" 
    id = Column(Integer , primary_key = True)
    name = Column(String)
    category = relationship("HAFAN" , back_populates = "cates")

base.metadata.create_all(engine)
