class ATM:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self,deposit):
        self.__balance += deposit
        print("balance after deposit",self.__balance)
    def withdraw(self,withdraw):
        if self.__balance<withdraw:
            print("Insufficiant balance")
        else:
            self.__balance -= withdraw
            print("balance after withdrawing",self.__balance)
S1=ATM(10000)
S1.deposit(1000)
S1.withdraw(5000)
print("balance after all ",S1.get_balance())