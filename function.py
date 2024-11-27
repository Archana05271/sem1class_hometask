#1
def create(argus):
 result=list(argus)
 return result
result=create(1,"circle",3.14,False,None)
print(result,end=" ")

#2
def fact(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
number = int(input())
print(f"The factorial of {number} is {fact(number)}")
#3
def product(a1,a2):
 result=a1*a2
 print("Product=",result)
a1=int(input())
a2=int(input())
product(a1,a2)
#4
def display(first_name,last_name):
 print(f"{last_name}.{first_name}")
first=input()
last=input()
display(first,last)
#5
def sqrt(s):
 result=s*s
 return result
n=int(input())
square=sqrt(n)
print("Square=",square)
