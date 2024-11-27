#1
def student_detail(Name,Age,Dep):
 print("Student Name:",Name)
 print("Student Age:",Age)
 print("Student Department:",Dep)
S_Name=input("Enter student name:")
S_Age=int(input("Enter student age:"))
S_Dep=input("Enter student department:")
student_detail(Name=S_Name,Age=S_Age,Dep=S_Dep)
#2
def food_details(food_items):
    print(food_items)
fo_type=input("Enter food type:")
it_name=input("Enter item name:")
it_cost=int(input("Enter item cost:"))
food_detail={"Food type":fo_type,"Item name":it_name,"Item cost":it_cost}
food_details(food_detail)
