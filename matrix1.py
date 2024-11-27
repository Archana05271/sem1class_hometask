#1
rows,cols = map(int, input("Enter number of rows and columns: ").split())
matrix = []
print()
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
result = []
for col in range(cols):
    if col % 2 == 0:
        for row in range(rows):
            result.append(matrix[row][col])
    else:
        for row in range(rows - 1, -1, -1):
            result.append(matrix[row][col])
print(" ".join(map(str, result)))
