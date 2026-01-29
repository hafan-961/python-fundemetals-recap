'''
In diamond problem order of return is from Class D -> B -> C ->  A


its like if the return is not there in D then it will chcek on B then if ist sitll not there then C and if not A
'''






''' ---------------------------------------------------------------------------------------------------'''

class A:
    def message(self):
        print("A")

class B(A):
    def message(self):
        print("B")
class C(A):
    def message(self):
        print("C")
class D(B,C):
    def message(self):
        print("D")


obj = D()
obj.message()