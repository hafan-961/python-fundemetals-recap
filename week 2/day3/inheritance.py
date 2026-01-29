# class animal:
#     def speak(self):
#         print("animal makes a sound")

# class Dog(animal):
#     def bark(self):
#         print("Dog barks")

# d = Dog()

# d.speak()
# d.bark()


#using super

# class animal:
#     def __init__(self,name):
#         self.name = name


# class dog(animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

# s = dog("lozack" , "husky")
# print(s.name)
# print(s.breed)


# multiple inheritance

# class Teacher:
#     def teach(self):
#         print("Teacher: Teaching subjects")


# class Coder:
#     def code(self):
#         print("Coder: Writing code")


# class Student(Teacher, Coder):
#     def study(self):
#         print("Student: Studying")

# s = Student()
# s.teach()   
# s.code()    
# s.study()   



class Teacher:
    def __init__(self, subject):
        self.subject = subject
        print("teacher constructor called")


class Coder:
    def __init__(self, language):
        self.language = language
        print("coder constructor called")


class Student(Teacher, Coder):
    def __init__(self, name, subject, language):
        self.name = name
        super().__init__(self, subject)
        Coder.__init__(self, language)
        print("student constructor called")


c = Student("hafan", "english", "python")




# class parent:
#     def __init__(self):
#         self.__x = 10

# class child(parent):
#     def show(self):
#         print(self.__x)

# obj = child()
# obj = show()