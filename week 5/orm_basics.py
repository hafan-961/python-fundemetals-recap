#import create_engine to connect the data base
from sqlalchemy import create_engine


#import declarative base 
from sqlalchemy.orm import declarative_base
'''create base class'''
base = declarative_base()  #base will be parent of all models 


#Refference 
'''
Table -> class
Rows -> object
column -> variables
'''
