#1
n=int(input())
sum=0
while n>0:#345|34|3
    sum=sum+n%10#0+5=5|5+4=9|9+3=12
    n=n//10#34|3|0(discard the last digit)
print(sum)
#2
n=int(input())

product=1
while n>0:#456|45|4
    product=product*(n%10)#1*6=6|6*5=30|30*4=120
    n=n//10#45|4|0
print(product)

#3
n=int(input())
for i in range(n,0,-1):#n=start,0=end,-1=decrement 1 by each time.
    print(i,end="")
