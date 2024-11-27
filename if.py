#1
a=int(input())
if(a%2)==0:
    print("Even")
else:
    print("Odd")
#2
a=int(input())
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
#3
mathematics=int(input())
physics=int(input())
chemistry=int(input())
total=mathematics+physics+chemistry
percentage=total/300*100
print(total)
print(f"{percentage:.2f}")
if percentage>90:
    print("Eligible")
else:
    print("Not Eligible")
#4
txt=input()
if txt==txt.upper():
    print("Uppercase")
elif txt==txt.lower():
    print("Lowercase")
else:
    print("combination of both")




