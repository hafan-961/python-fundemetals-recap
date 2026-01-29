#ENCAPSULATION
'''it will hide the 
we have to acess an ensapsulated data through method which is inside the class'''

# class student:
#     def __init__(self,marks):
#         self.__marks = marks

#     def ok(self):
#         return self.__marks

# s1 = student(100)
# print(s1.ok())


'''create a bank class where balance is hidden '''

class bank:
    def __init__(self, bank_balance ):
        self.__balance = bank_balance      #(data hiding)

    def get_bal(self):                 #helps in acessing the private vairable  (acess the data)
        return self.__balance

    def change_bal(self , new_bal):    #it chanhes the balance
        self.__balance = new_bal


s1 = bank(100000)
s1.change_bal(90)
print(f"your balance is : {s1.get_bal()}")
