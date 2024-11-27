#1 Calculate the sum of the array elements
#2 Find the occurrence of an element in the array
#3 Largest element in the array
#1
import array as arr
a=arr.array('i')
su = 0
n=int(input("Enter the integer to be inserted="))
for i in range(n):
    a.append(int(input()))
for e in range(n):
    su+=a[e]
print("sum =",su)
#2
import array as r
s=r.array('i')
ele=int(input())
count=0
for i in range(ele):
    s.append(int(input()))
search=int(input("Enter element to be searched:"))
for i in range(ele):
    if search==s[i]:
        count+=1
print(count)

#3
import array as a
l=[]
largest=0
d=a.array('i',l)
elem=int(input())
for i in range(elem):
    l.append(int(input()))
for i in range(elem):
    if l[i]>largest:
        largest=l[i]
print(largest)  
