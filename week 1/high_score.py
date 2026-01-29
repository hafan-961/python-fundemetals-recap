file_name = "high_score.txt"
score = 0

high_score = 0

def load_high_score():
    global high_score
    try:
        #open a file in read mode
        file= open(file_name , "r")
        high_score = int(file.read())
        file.close()

    except:
        pass

#Save high score

def save_high_score():
    #open the file in wirte mode
    file = open(file_name , "w")
    file.write(str(high_score))
    file.close()

#Play Quiz

def play_quiz():
    global score
    questions = ["what is output of print (2-3 ?)" , "which datatype stores True/False" , "which keyword is used o fetch global variable in thi function ?"]
    answers = ["5" , "bool" , "global"]
    for i in range(len(questions)):
        print("\n Q" , questions[i])
        user_answer =  input("Your answer:")
        if user_answer == answers[i]:
            score = score+1
            print("Correct")
        else:
            print("Wrong!!")
def main():
    #Global allows updating same high score 
    global high_score
    #load previous high score
    load_high_score()
    #ask player the name 
    name = input("enter the name: ")
    #start Quiz

    play_quiz()
    #print final score

    print("\nQuiz over")
    print(name, "Your scoreis : " , score)
    #compare score with high score

    if score > high_score:
        high_score  = score
        save_high_score()
    else:
        print("high scoreis :" , high_score)

main()