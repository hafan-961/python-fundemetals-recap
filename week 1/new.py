class college:
    def __init__(self, s_name , s_roll):
        self.student = s_name
        self.roll = s_roll

s1 = college("hafan" , 25)
s2 = college("elton" ,45)

print(s1.student , s1.roll)
s2.name = "eljo"
print(s2.name , s2.roll)

#creata a class student where total stuent is a class attribute and then we ahve to increase this count whenever object is created 

class student:
    total_students = 0
    def __init__(self,s_name,roll):
        self.name = s_name
        self.roll = roll
        student.total_students += 1

s1 = student("hafan"  , 34)
s2 = student("eljo" , 30)
s3 = student("elton" , 32)
print(student.total_students)
