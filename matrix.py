#1
c = int(input())
a = []
for i in range(c):
    a.append(list(map(int, input().split())))

odd = True
even = True
for i in range(c):
    for j in range(c):
        if a[i][j] % 2 == 0:
            odd = False
        if a[i][j] % 2 != 0:
            even = False

if odd or even:
    print("Yes")
else:
    print("No")

#2
c = int(input())
arr = []
for i in range(c):
    arr.append(list(map(int, input().split())))
forward = 0
backward = 0
for i in range(c):
    forward += arr[i][i]  # Sum of the forward
    backward += arr[i][c - i - 1]  #Sum of the backward(3-1-1)
if  forward== backward:
    print("Yes")
else:
    print("No")
#3
n=int(input())
matrix=[]
for _ in range(n):
    m=list(map(int,input().split()))
    matrix.append(m)
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(n):
    matrix[i].reverse()
for k in matrix:
    print(*k)

