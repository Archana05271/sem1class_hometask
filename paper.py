import random
def start():
    print("****ROCK PAPER SCISSORSS****")
    print("Enter your choice")
    print("1.ROCK \n2.PAPER \n3.SCISSOR")
    user_choice=int(input())
    comp_choice=random.randint(1,4)

    if comp_choice==1:
        print("Computer choice is : Rock")
    elif comp_choice==2:
        print("Computer choice is : Paper")
    else:
        print("Computer choice is : Scissor")

    if(user_choice==1 and comp_choice==3):
        print("You Won!!!")
    elif(user_choice==2 and comp_choice==1):
        print("You Won!!!")
    elif(user_choice==3and comp_choice==2):
        print("You Won!!!!")
    elif(user_choice==comp_choice):
        print("Tie!!!")
    else:
        print("Computerv won !!!")
    play=input("Do you want to continue? Yes/No")
    if play=="Yes":
        start()
    else:
        print("Thank you for playing")
start()
    
