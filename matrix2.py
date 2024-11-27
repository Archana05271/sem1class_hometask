#2
row=int(input())
col=int(input())
arr=[]
for i in range(row):
    a=list(map(int,input().split()))
    arr.append(a)
for i in range(col):
    left=0
    right=i
    while left<row and right>=0:
        print(arr[left][right],end=" ")
        left+=1
        right-=1
    print()
for i in range(1,row):
    left=i
    right=col-1
    while left<row and right>=0:
        print(arr[left][right],end=" ")
        left+=1
        right-=1
    print()
