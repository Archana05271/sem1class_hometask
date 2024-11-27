n=int(input())
m=n
sum=0
while n>0:#18|1#32|3
    num=n%10#8|1#2|3
    sum+=num#0+8|8+1=9#0+2|2+3=5
    n=n//10#1|0#3#0
if sum%m==0:
    print(f"{m} is a Harshad Number")
else:
    print(f"{m} is not a Harshad Number")
    
    
