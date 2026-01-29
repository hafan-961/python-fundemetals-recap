'''
Dont rely on Inheritance
use object or other class
'''

class Address:
    def __init__(self,city):
        self.city = city
    def show_address(self):
        print(f"city: {self.city}")
    
class student:
    def __init__(self,name,city):
        self.name = name 
        #composition: creating👇
        #creating object of address class inside student class
        self.address = Address(city)  
 
    def show_student(self):
        print("Name" , self.name)
        #using objct of another class
        self.address.show_address()

s = student("Karan" , "Delhi")
s.show_student()