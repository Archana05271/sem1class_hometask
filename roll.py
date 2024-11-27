#1
import random
while True:
    user_input=input("Enter any case:")
    match user_input:
        case "take":
            result=random.randrange(1,6)
            print(result)
        case "exit":
            print("exit")
            quit()
        case _:
            print("Case is invalid")
            break
#2
        
import random
restaurant=["MRA","Good morning","Annapoorna","KFC","Kumar Cafe","KFC","Surya Fast Food"]
while True:
    user_input=input("Enter any case:")
    match user_input:
        case "take":
            result=random.choice(restaurant)
            print(result)
        case "bye":
            quit()
        case _:
            print("Invalid input")
            break
