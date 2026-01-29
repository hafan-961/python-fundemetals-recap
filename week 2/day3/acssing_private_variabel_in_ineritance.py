# # acessing private varaible of parent class by using method 
# class parent:
#     def __init__(self):
#         self.__x = 10

# class child(parent):
#     def show(self):
#         print(self._parent__x)     #in private we have to use parent class name before varaible 

# o1 = child()
# o1.show()



''' 3 Modes of varaible 

public  :-  x
private :-  __x
protected :- _x

'''

# acessing protected varaible of parent class

class parent:
    def __init__(self):
        self._x = 10

class child(parent):
    def show(self):
        print(self._x)

o1 = child()
o1.show()

#acessing protected varaible of multipe inhertited class
# class parent:
#     def __init__(self):
#         self._x = 10

# class boy:
#     def show(self):
#         self._x = 30

# class child(parent,boy):
#     def show(self):
#         boy.show(self         c                    )
#         print(self._x)

# o1 = child()
# o1.show()