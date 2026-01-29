class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name
        self._balance = balance
    
    def deposit(self,amount):
        self._balance += amount
        return self._balance

    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            return "Infsufficient balance"
    
    def get_balance(self):
        return self._balance
    
    def calculate_interest(self):
        pass

class SavingAccount(BankAccount):
    def calculate_interest(self):
        interest = self._balance * 0.04
        return interest

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0

class BankApp:
    def __init__(self):
        self.account = None
    def create_account(self,acc_no,name,balance,acc_type):
        if acc_type == "savings":
            self.account = SavingAccount(acc_no, name , balance)
        else:
            self.account = CurrentAccount(acc_no, name , balance)
        
        return "Account created sucessfully"

    def deposit_money(self,amount):
        return self.account.deposit(amount)
    def withdraw_money(self,amount):
        return self.account.withdraw(amount)
    def check_balance(self):
        return self.account.get_balance()
    def get_interest(self):
        return self.account.calculate_interest()

app = BankApp()
print(app.create_account(101,"Rahul" , 10000, ("Savings".lower())))
print("balance after deposite " , app.deposit_money(0))
print("balace after withdraw: " , app.withdraw_money(0))
print("current balance is : " , app.check_balance())
print("Interest is : " , app.get_interest())


