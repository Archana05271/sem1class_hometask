#1
students = int(input("Enter the number of students: "))
subjects = int(input('Enter the number of subjects: '))
sub = ["Maths", "English", "Science"]
grades = []

for i in range(students):
    student_grades = []
    print(f"\nEnter grades for Student {i + 1}:")
    for j in range(subjects):
        grade = int(input(f"{sub[j]}: "))
        student_grades.append(grade)
    grades.append(student_grades)

# average
print("\nAverage grades for each student:")
for i, student_grades in enumerate(grades):
    student_average = sum(student_grades) / len(student_grades)
    print(f"Student {i + 1}: {student_average:.2f}")

# highest grade in each subject
print("\nHighest grade in each subject:")
for j in range(subjects):
    highest_grade = max(grades[i][j] for i in range(students))
    print(f"{sub[j]}: {highest_grade}")

# overall class average
to_sum = sum(sum(student_grades) for student_grades in grades)
to_grades = students * subjects
class_average = to_sum / to_grades
print(f"\nOverall class average: {class_average:.2f}")

#2
m, n = map(int,input().split())
products = []
for i in range(m):
    row = list(map(int, input().split()))
    products.append(row)

total = [sum(rows) for rows in products]
print("Total quantities of each product: ")
for i, j in enumerate(total):
    print(f"Product {i + 1}: {j}")

product = int(input("Product to check: "))
max_quantity = max(products[product - 1])
section = products[product - 1].index(max_quantity) + 1
print(f"Section with highest quantity for product {product}: Section {chr(64 + section)}")

lowest = min(total)
lowest_index = total.index(lowest) + 1
print(f"Product with the lowest total quantity: Product {lowest_index}")
