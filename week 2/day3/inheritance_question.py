# acessing private varaibel using getter ans setter

# class person:
#     def __init__(self):
#         self.__name = "hafan"

#     def get_name(self):
#         return self.__name

# class student(person):
#     def show_name(self):
#         print(self.get_name())


# o1 = student()
# o1.show_name()

#another style

# class person:
#     def __init__(self,name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

# class student(person):
#     def show_name(self):
#         print("my name is : " , self.get_name())


# o1 = student("hafan")
# o1.show_name()


''' 
Q2) 
'''


class account():
    def __init__(self,balance):
        self._balance = balance

    def show_balance(self):
        return self._balance # getter 

    def set_balance(self,amount):
        self._balance += amount      #setter

class saving(account):
    def add_money(self):        
        amount = int(input("Enter the amount you want to deposite: "))
        self.set_balance(amount)
        print("updated balance: " , self.show_balance())
        


o1 = saving(100)
o1.add_money()