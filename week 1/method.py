'''Q.what is method 
    ans). a function whihc is purley related to the objects'''


# class student:
#     def __init__(self,name):
#         self.name = name
    
#     def hello(self):
#         print("welcome" , self.name)

#     @staticmethod
#     def college_name():
#         print("this is lpu")


# s1 = student("hafan")
# s1.college_name()

# s1.hello()




'''create a class student which have object attribute name and marks and there 
is a normal methond we have to make which will display (display method)

'''

class student:
    def __init__ (self,name ,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"hi {self.name} your marks is {self.marks}")

s1 = student("hafan" , 89)
s2 = student("muhammed" , 78)

s1.display()
s2.display()
