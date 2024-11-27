import math
bill=int(input())
bill1=int(input())
bill2=int(input())
total=(bill+bill1+bill2)
if total>400:
    tax=math.trunc(6.75/100*total)
    tip=total+tax
    tip1=math.trunc(10/100*tip)
    print(total)
    print(tax)
    print(tip1)
    print(total+tax+tip1)
else:
    print(total)
