#1
sr=int(input("Start range="))
er=int(input("End range="))
print("Odd numbers:",end="")
for i in range(1,11):
    if i%2!=0:
        print(i,end="")
print("\nEven numbers:",end="")
for i in range(1,10):
    if i%2==0:
        print(i,end="")
#2
Word=input("Enter a String")
Reverse_Word=""
for i in range(len(Word)-1,-1,-1):
    Reverse_Word+=Word[i].upper()
print(Reverse_Word)


#3

Sales_figures=[150,-45,90,-75,400,-60,500,-98]
successful_sales=0
returns=0
for i in Sales_figures:
    if i>0:
        successful_sales+=1
    else:
        returns+=1
print("Number of successful sales:",successful_sales)
print("Number of returns or losses:",returns)
        
    

    

   
