# class Human:
#     def speak(self):
#         print("Huaman is speaking")

# class Baby:
#     def speak(self):
#         print("baby is crying ")

# class Dog:
#     def speak(self):
#         print("Dog is barking")

# #polymorphism in action 

# h = Human()
# b = Baby()
# d = Dog()

# h.speak()
# b.speak()
# d.speak()


# class Car:
#     def write(self):
#         print("i am driving car")

# class Bike:
#     def write(self):
#         print("i am driving Bike")

# class Truck:
#     def write(self):
#         print("i am driving Truck")

# #polymorphism in action 

# h = Car()
# b = Bike()
# d = Truck()

# h.write()
# b.write()
# d.write()

'''create a class person with method Role , then create two child of that class student and teacher 
create another class assistant that inherit from both student and teacher 

'''

class person:
    def role(self):
        print("I am a person")



class student(person):
    def role(self):
        print("I am a student")

class teacher(person):
    def role(self):
        print("I am a teacher")

class assistance(student,teacher):
    pass

obj = assistance()
obj.role()