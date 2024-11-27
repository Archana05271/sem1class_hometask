n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
sum = 0
i = 0
while i <= n:
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum += (x**i)/fact
    i += 1
print(int(sum))
