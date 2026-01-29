''' create a class student in which the normal method is show names and 
roll  and static method is show college name  '''

class student:
    def __init__(self, name , roll):
        self.name = name
        self.roll = roll

    @staticmethod
    def college():
        return "lpu"

s1 = student("hafan" , 45)
s2 = student("elton" , 46)

print(s1.name ,s1.roll, s1.college())



