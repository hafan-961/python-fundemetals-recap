'''Flow of project
load the old expense from the file 
show menu 
1. add expnse
2. view expense
3. total expense
4. exit
user selects one option 
function runs
save data
repeat


load_data -> reads old expense form file 
save_data -> saves expense
'''

file_name = "expense.txt"
expenses = []

#Load data
def load_data():
    global expenses
    try:
        file = open(file_name , "r")
        lines = file.readlines()
        file.close()
    
    for line in lines:
        line = line.strip()
        amount , category , note = line.split(",")
        expense = {
            "amount" : int(amount),
            "category" : category,
            "note" : note
        }
        expense



        