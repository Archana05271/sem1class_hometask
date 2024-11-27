grades=[89,45,65,75]
try:
    average = sum(grades) / len(grades)
    print("Average grade:", average)
except ZeroDivisionError:
    print("List can't be empty")
