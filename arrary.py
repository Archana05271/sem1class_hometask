#1
N1 = int(input("first list"))
L1 = []
for i in range(N1):
    name = input("Enter student name ")
    L1.append(name)
N2 = int(input(" second list "))
L2 = []
for i in range(N2):
    grade = int(input("Enter grade"))
    L2.append(grade)
for i in range(N1):
    print(L1[i], L2[i])


#2
n = int(input("Enter the numbers: "))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
min_element = arr[0]
for num in arr:
    if num < min_element:
        min_element = num
print( "Minimum element=",min_element)
#3
import array as arr
n1 = int(input("for the first array: "))
arr1 = []
for i in range(n1):
    num = int(input("Enter element"))
    arr1.append(num)
n2 = int(input("for the second array: "))
arr2 = []
for i in range(n2):
    num = int(input("Enter element"))
    arr2.append(num)
arr1.sort(reverse=True)
arr2.sort(reverse=True)
merged = arr1 + arr2
merged.sort(reverse=True)
print("Merged array in descending order:", merged)
