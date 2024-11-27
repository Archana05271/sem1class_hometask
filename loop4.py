#1
n=int(input())#123
rev=0
while n>0:#123|12|1
    r=n%10#3|2|1
    rev=(rev*10)+r#0+3=3|30+2=32|320+1=321
    n=n//10#12|1|0
print(rev)

#2
n=int(input())
m=n
sum=0
while n>0:#153|15|1
    r=n%10#3|5|1
    sum=sum+r*r*r#27|152|153
    n=n//10#15|1|0
if sum==m:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

