#1
num_products = int(input())
num_days = int(input())
d_array = []
for i in range(num_products):
    sales_input = input()
    sales_row = list(map(int, sales_input.split()))
    d_array.append(sales_row)
total_sales = 0
for row in d_array:
    total_sales += sum(row)
print(total_sales)

#2
num_rows = int(input())
num_cols = int(input())
d_array = [list(map(int, input().split())) for i in range(num_rows)]
element_to_find = int(input("Enter the element to be found: "))
found = False
for i in range(num_rows):
    if element_to_find in d_array[i]:
        print(f"Found at ({i},{d_array[i].index(element_to_find)})")
        found = True
        break
if not found:
   print("Not found")"""

#3
num = int(input("Enter the number of rows/columns: "))
arr = []
for i in range(num):
    l = list(map(int, input().split()))
    arr.append(l)
print("Original matrix:")
for row in arr:
    print(row)
arr1 = [[] for _ in range(num)]
for i in range(num):
    for j in range(num):
        arr1[i].append(arr[j][i])
print("Transposed matrix:")
for row in arr1:
    print(row)

"""#4

num_rows = int(input("Enter number of rows: "))

num_cols = int(input("Enter number of columns: "))
seats = []
print()
for i in range(num_rows):
    row = list(map(int, input().split()))
    seats.append(row)
print("Theater Seating Chart:")
for row in seats:
    display_row = ""
    for seat in row:
        if seat == 0:
            display_row += "O "
        else:
            display_row += "X "
    print(display_row.strip())"""


