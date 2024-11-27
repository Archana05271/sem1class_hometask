#1
n = int(input("Enter a number: "))
temp = n
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if n == rev:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
#2
n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
sum = 0
i = 0
while i <= n:
    fact = 1
    for j in range(1, i+1):
        fact= j
    sum += (x**i)/fact
    i += 1
print(int(sum))
#3
num = int(input("Enter a number: "))
product = 1
while num > 0:
    digit = num % 10
    product *= digit
    num //= 10
print("Product of digits: ", product)
#4
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(f"Factorial of {n} is ",i)
#5
num=int(input()) 
if num<2:
      f=False
else:
    f=True
    for i in range(2,num):
        if num%i==0:
            f=False
            break
    if f:
        print("Its a Prime")
    else:
            print("Not a Prime")
#10
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


#11
for i in range(100,501):
    if i%11==0 and i%2!=0:
        print(i)


