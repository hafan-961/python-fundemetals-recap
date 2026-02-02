'''
Design a console based library management system a 
 a libraryitem is the base(abstract) idea
 book and magazine aree differenct type of items 
 borrowing rules behave diff for each of them
 a liabraryApp conroles items (HAS-A)
 use oops concept and return value , not only print
 '''
class Library_Item:           #Abstract class
    def __init__(self, student_id, name, member, days):
        self.student_id = student_id
        self._name = name        # encapsulated
        self._member = member     # encapsulated
        self._days = days         # protected

    def is_member(self):
        return self._member

    def calculate_rent(self):
        pass   # only rule 

#Interface class
class interface:
    def calculate_rent(self):
        pass

class Book(Library_Item):   #Inhertitance
    def __init__(self, student_id, name, member, days):
        super().__init__(student_id, name, member, days)  

    def calculate_rent(self):     # polymorphism
        if self._member == "yes":
            return 0
        else:
            return self._days * 50


class Magazine(Library_Item):  #Inheritance
    def __init__(self, student_id, name, member, days):
        super().__init__(student_id, name, member, days)

    def calculate_rent(self):    #polymorphism
        if self._member == "yes":
            return 0
        else:
            return self._days * 30

#composition class
class LibraryApp:
    def __init__(self):
        self.item = None

    def item_taken(self, item_type, student_id, name, member, days):
        if item_type == "Book":
            self.item = Book(student_id, name, member, days)
        elif item_type == "Magazine":
            self.item = Magazine(student_id, name, member, days)

        print("Item issued")

    def get_rent(self):
        return self.item.calculate_rent()



app = LibraryApp()
app.item_taken("Book", 1, "hafan", "no", 5)
print(app.get_rent())

app2 = LibraryApp()
app2.item_taken("Magazine", 1, "hafan", "no", 3)
print(app2.get_rent())

