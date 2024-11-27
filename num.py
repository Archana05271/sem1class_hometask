m=int(input())
n=int(input())
special=0
for i in range(m,n+1):
    first=i//10
    second=i%10
    add=first+second
    pro=first*second
    spe=add+pro
    if spe==i:
        special=i
        print(special)
    
