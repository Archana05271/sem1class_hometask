#1
num=int(input())
if num%3==0 and num%5==0:
    print("Divisible by both")
elif num%5==0:
    print("Divisible by 5")
elif num%3==0:
    print("Divisible by 3")
#2
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
    
#3
weight=float(input())
height=float(input())
BMI=weight/height**2
print(f"{BMI:.1f}")
if(BMI<16):
    print("Severe Thinness")
elif BMI>16 and BMI<17:
    print("Moderate Thinness")
elif BMI>17 and BMI<18.5:
    print("Mild Thinness")
elif BMI>18.5 and BMI<25:
    print("Normal")
elif BMI>25 and BMI<30:
    print("Overweight")
elif BMI>30 and BMI<35:
    print("Obese Class I")
elif BMI>35 and BMI<40:
     print("Obese Class II")
else:
    print("Obese Class III")

    

    
