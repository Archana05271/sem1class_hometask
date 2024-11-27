#1
num=int(input())#123
rem=num%10#123%10=3
rev=(num//10)%10#123//10=12|12%10=2
n=num//100#123//100=1
rev=rem*100+rev*10+n#321
print(rev)

#2
n=int(input())
m=n
sum=0
while n>0:#153|15|1
    r=n%10#3|5|1
    sum=sum+r*r*r#0+27|27+152|152+1
    n=n//10#15|1|0
if sum==m:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

