Word=input("Enter a String")
Reverse_Word=""
for i in range(len(Word)-1,-1,-1):
    Reverse_Word+=Word[i].upper()
print(Reverse_Word)
