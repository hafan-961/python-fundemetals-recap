student = {}
while True:
    print("\n----Student Management System---")
    print("1. Add Student")
    print("2 . View Students")
    print("3 .Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter the choice here (1-5): ")

    if choice == '1':
        name = input('enter the student name: ')
        age = int(input("enter the student age : "))
        number = int(input("Enter the studnet number:"))
        student[name] = {'age' : age, 'number' : number}
        print(f"Student {name} added successfully.")

    elif choice == '2':
        if student:
            print("\n all students: ")
            for name,  info in student.items():
                print(f"Name: {name}, Age: {info['age']} , Number: {info['number']}")
        else:
            print("No students found.")
    
    elif choice == '3':
        name = input("Enter student name to search: ")
        if name in student:
            info = student[name]
            print(f"Name: {name}, Age: {info['age']}, Number: {info['number']}")
        else:
            print(f"Student {name} not found.")
    
    elif choice == '4':
        name = input("Enter student name to delete: ")
        if name in student:
            del student[name]
            print(f"Student {name} deleted successfully.")
        else:
            print(f"Student {name} not found.")

    elif choice == '5':
        print("secission exited")
        break
    else:
        print("Invalid choice try again")




        