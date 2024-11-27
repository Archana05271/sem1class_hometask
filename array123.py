num=int(input())
a=[]
for i in range(num):
    a.append(int(input()))
negative=[]
postive=[]
for c in a:
    if c<0:
        negative.append(c)
    else:
        postive.append(c)
        print(f"{negative+postive}")
#2
start_char = 65 
char_count = 1
rows = 4
for i in range(1, rows + 1):
    for j in range(char_count):
        print(chr(start_char), end=" ")
        start_char += 1
    print()
    char_count += 1
#4
for x in range(3, 9, 2):
    print(x * 10)
#5
access_logs=[100,200,300,100,200,400]
se=set()
dup=set()
for user_id in access_logs:
    if user_id in se:
        dup.add(user_id)
    else:
        se.add(user_id)
for user_id in dup:
    print(user_id,end=' ')
