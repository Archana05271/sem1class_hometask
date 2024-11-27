#5
login_details = {'achu23': '456','appu34': 'pas','asin23': '856'}
username = input("Enter the username:")
password = input("Enter the password:")
if username not in login_details:
    print("Invalid username")
else:
    if login_details[username] == password:
        print("Successfully logged in")
    else:
        print("Incorrect password")
#3
number = input("Number=")
replace = input(" To replace= ")
digit = input("Replace= ")
if len(replace) != 1 or len(digit) != 1:
 print(" digit must be single characters")
else:
 modified_number = number.replace(replace, digit)
 print("Modified number =", modified_number)

#2
n = int(input("Enter number of elements: "))
array = []
for _ in range(n):
 array.append(int(input()))
array.sort(reverse=True)
if len(array) < 2:

 print("Array does not have enough elements ")
else:
 second_largest = array[1]
 print("Second largest element:", second_largest)
#1
N = int(input("Enter the number of elements: "))
arr = []
for _ in range(N):
    arr.append(int(input()))
y = int(input("Enter the element to check: "))
count_y = arr.count(y)
if count_y > N // 2:
 print(f"{y} is a majority element")
else:
 print(f"{y} is not a majority element")
    

