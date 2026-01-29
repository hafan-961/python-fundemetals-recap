class Student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.mark = marks

s1=Student("shan", 45)
s2 = Student("HAFAN" , 20)

print(s1.name, s1.mark)
print(s2.name , s2.mark)

class car:
    showroom = "lovely_autos"
    def __init__(self,model , price):
        self.model = model
        self.price = price

s1 = car("brezza" , 1000)
s2 = car("vento" , 3000)

print(s1.showroom ,s1.model , s1.price)
print(s2.showroom , s2.model , s2.price)

car.showroom = "non" #chaingin class attribute

print(s1.showroom , s1.model , s1.price)
print(s2.showroom , s2.model , s2.price)