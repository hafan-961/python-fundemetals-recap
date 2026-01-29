''' 
create a class course 
and create two methond course info (commom logic) and duration 

create an interface exam interface 
it has a method exam type 

we have a class named python class
course  and examInterface  are parameters 

methods are duration and exam_type
'''

class course:
    def course_info(self):
        print("course info not available now , please come again later 😂")
    def duration(self):
        pass

class exam_interface:
    def exam_type(self):
        pass

class python(course , exam_interface):
    def duration(self,duration):
        print("the duration of exam is:" , duration , "hr")
    def exam_type(self,exam_type):
        print("type of examination is: " , exam_type)

class java(course , exam_interface):
    def duration(self,duration):
        print("the duration of exam is:" , duration , "hr")
    def exam_type(self,exam_type):
        print("type of examination is: " , exam_type)


obj = python()
obj.duration(3)
obj.exam_type("MCQ")
obj.course_info()



