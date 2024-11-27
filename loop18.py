#1
n = int(input())#4
a, b = 1, 1
ev_fibnocci_no = []#[2,8,34,144]
while len(ev_fibnocci_no) <= n:
    a, b = b, a + b#1,2|2,3|3,5|5,8|8,13|13,21|21,34|34,55|55,89|89,144
    if b % 2 == 0:#2|3|5|8|13|21|34|55|89|144
        ev_fibnocci_no.append(b)
print(ev_fibnocci_no[n-1])
#2
plots = int(input())
areas = list(map(int, input().split()))
count = 0

for area in areas:
    root = int(area ** 0.5)
    if root * root == area:
        count += 1

print(count)
