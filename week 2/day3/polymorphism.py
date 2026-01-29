''' polymorphism
poly =  many 
morph = form 

same name , different behaviour , depsnes on object 

'''

class dog:
    def speak(self):
        print("dog is speaking")
        
class cat:
    def speak(self):
        print("MEOW")


o1 = dog()
o2 = cat()
o1.speak()
o2.speak()