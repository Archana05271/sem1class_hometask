#1
ro,co=map(int,input().split())
m=[]
for _ in range(ro):
    a=list(map(int,input().split()))
    m.append(a)
m1=[]
for _ in range(co):
    b=list(map(int,input().split()))
    m1.append(b)
res=[]
for i in range(ro):
    rows=[]
    for j in range(co):
        rows.append(m[i][j]+m1[i][j])
    res.append(rows)
for row in res:
    print(*row)
    
#2
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
#3
r, c = map(int, input().split())
elements = []
for _ in range(r):
    r = list(map(int, input().split()))
    elements.extend(r)
max_value = max(elements)
print(f"Maximum element =",max_value)
#4
n = int(input())
arr = []
for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)

is_symmetric = True
for i in range(n):
    for j in range(n):
        if arr[i][j] != arr[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print("Symmetric matrix")
else:
    print("Not symmetric matrix")


