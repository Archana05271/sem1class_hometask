#1prime
n=int(input("Enter the no"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime")
else:
    print("not Prime")
#2divisible
n=int(input("Enter the no"))
if n%11==0:
    print(n,"is divisible by 11")
else:
    print(n,"is not divisible by 11")
#3fibanocci
n1=0
n2=1
count=0
if n<=0:
    print("Enter a positive integer")
elif n==1:
    print(n1)
else:
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
#4factorial
n=int(input("Enter the no"))
f=1
for i in range(1,n+1):
    f*=1
    print("Factorial of"{n}"is"{f})
#5fcators
n=int(input("Enter the no"))
for i in range(1,n+1):
    if n%i==0:
        print(i)

        
