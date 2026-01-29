class Engine:
    def start(self):
        print("engine started")


class Car:
    def __init__(self):
        self.engine = Engine()
    # def c(self):
    #     self.engine = Engine()
    def drive(self):
        # self.c()
        self.engine.start()
        print("car is driving")


ob = Car()
ob.drive()

class subject:
    def teach(self):
        print("subject is math")

class teacher:
    def __init__(self):
        self.omg = subject()
    def go(self):
        self.omg.teach()
        print("lets goooooo")

ob = teacher()
ob.go()