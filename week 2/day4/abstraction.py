'''
|------------ABSTRACTION------------|

.define the rule
show what to do 
hides how to do 
mainly used in big problems
'''
'''
empty  method  is present in parent class
child class will complete method body 
'''

# class payment:
#     def pay(self,amount):             #just rules 
#         pass

# class upi(payment):
#     def pay(self,amount):                         #excecuted by derived (child) class
#         print("paid using UPI: ",amount)

# class card:
#     def pay(self,amount):
#         print("the amount payed by cash is: ",amount)
# class cash:
#     def pay(self,amount):
#         print("the amount payed by cash is: ",amount)

# obj = upi()
# ob = cash()
# obj.pay(12)
# ob.pay(100)


class shape:
    def area(self, l ,b):
        pass

class square(shape):
    def area(self,l,b):
        print("area of square is: ",l * l)

class rectangle(shape):
    def area(self,l,b):
        print("area of rectangle: ",l*b)
class triangle(shape):
    def area(self,l,b):
        print("area of traingle is: ",(1/2 ) * (l*b))

obj1 = rectangle()
obj2 = square()
obj3 = triangle()

obj1.area(10,20)
obj2.area(10,20)
obj3.area(10,20)

'''Abstraction can be combination of both incomplete method and complete method'''