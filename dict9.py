grade={"abhi":[90,97,85],"akshara":[95,93]}
student="akshara"
new_grade=int(input())
if student in grade:
    grade[student].append(new_grade)
else:
    grade[student]=[new_grade]
print(grade)

g="abhi"
if g in grade:  
    grade_value=grade[g]  
    average=sum(grade_value)/len(grade_value)
else:
    average="Student not found"
print(f"{average:.2f}")
s="abhi"
if s in grade:  
    del grade[s]
else:
    print("Student not found")
#1a) Create a Tuple with a Single Element
tuple1= (5,)
print(tuple1)
#2Multiply a Tuple by an Integer
tuple2 = (1, 2, 3)
multiply = tuple2 * 3
print(multiply)
#3 get the index 
tuple3 = (10, 20, 30, 40)
index = tuple3.index(30)
print(index)
#4Modify an Element
my_tuple = (10, 20, 30)
l = list(my_tuple)
l[1] = 25
modified_tuple = tuple(l)
print(modified_tuple)
#5Convert a Tuple to a String
my_tuple = (1, 2, 3, 4)
string = str(my_tuple)
print(string)
#6 Maximum and Minimum 
my_tuple = (4, 1, 7, 3, 9)
max_value = max(my_tuple)
min_value = min(my_tuple)
print("Maximum:", max_value)  
print("Minimum:", min_value)
#7Count
my_tuple = (1, 2, 2, 3, 2, 4)
count = my_tuple.count(2)
print(count)
#8 Nested tuple #9 accessing the element 
nested_tuple = ((1, 5, 6), ('x', 'y', 'z'))
element = nested_tuple[0]
print(element)  
#10 delete 
tuple = (10, 20, 30, 40)
l = list(my_tuple)
del l[1]
n_tuple = tuple(l)
print(n_tuple)







