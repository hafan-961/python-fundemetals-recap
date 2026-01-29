#file = open("data.txt" , "mode-> r,w,a")






# file = open("student.txt" , "w")
# file.write("Name : Rahul \n")
# file.write("course : python \n")
# file.close()

# file = open("student.txt" , "a")
# file.write("mark : 29 \n")
# file.close()

# file = open("student.txt" , "r")
# data = file.read()
# print(data)
# file.close()

# with open("student.txt" , "r") as file:
#     data = file.read()
#     print(data)

# file = open("student.txt" , "r")
# data2 = file.readlines()
# print(data2)
# for line in file:
#     print(line)





# file = open("student.txt" , "r")
# data = file.read()
# print(len(data))
# file.close()


# file =  open("data.txt" , "w")
# file.write("hafan")
# file.close()

# file =  open("data.txt" , "r")
# data = file.read()
# count = data.lower().count("a")
# print("word cound: " , count)
# data = data.replace("hafan" , "charan")
# print(data)
# file.close()

# printing first 10 charasters in a file 


file = open("data.txt" , "w")
file.write("kgf\n")
file.write("Avengers\n")
file.write("Spoider man\n")
file.close()

file = open("data.txt" , "r")
data = file.read()
first_ten = data[:10]
print(first_ten)


