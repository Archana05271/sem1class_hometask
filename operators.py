#1
d=int(input())
e=int(input())
if d<e:
    print(d)
else:
    print(e)
#2
p=float(input())
r=float(input())
t=float(input())
a=p*(1+r/100)**t
com=int(a-p)
print(com)

#3
d=int(input())
e=int(input())
print(e,d)

#4
L=[12,34,45,56,67]
if 34 in L:
    print("Present")
else:
    print("Not Present")

#5
s=("she was a naughty girl")
if "good" not in s:
    print("True")
else:
    print("False")
