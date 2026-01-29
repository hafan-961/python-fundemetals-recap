#ABSTRACTION
'''there will be rules and work'''
class payment:
    def initilize(self):        #in abstracion logical method can be written
        print("Initilized")
    def pay(self,amount):
        pass

class card(payment):
    def pay(self,amount):
        print("the amount payed by card is:" , amount)
class upi(payment):
    def pay(self,amount):
        print("the amount payed by upi is:" , amount)

obj = card()
obj.initilize()
obj.pay(100)


#INTERFACE
'''100 rule no work'''
class payment:
    def pay(self,amount):        #only empty method is allowed in interface 
        pass

class card(payment):
    def pay(self,amount):
        print("the amount payed by card is:" , amount)
class upi(payment):
    def pay(self,amount):
        print("the amount payed by upi is:" , amount)

obj = card()
obj.pay(100)