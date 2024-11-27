#A
L=[10,45,1,67,56]
L.sort()#a
print("List in ascending order",L)
L.reverse()#b
print("List in descending order",L)
#B
S={10,20,30,40,50}
S1={50,60,70,80,90}
S2=S1.intersection(S)#a
print("Common element in a set",S2)
S3=S1.symmetric_difference(S)#b
print("Uncommon element in a set",S3)
S.remove(40)#c
print("Removing a data",S)
#C
T=("Apple","Orange","Mango","Grapes")
L=list(T)#a
L.append("Lemon")
print("Append",L)
L.remove("Orange")
print("Remove",L)
T=tuple(L)
print(T)
#D
Text=("Anu is a naughty girl")
a=Text.index("l")#a
print(a)
b=Text.replace("Anu","Arana")#b
print(b)
c=Text.lstrip()#c
print(c)
  
            

