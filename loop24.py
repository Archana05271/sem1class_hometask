#1
m_string = input(" main string: ")
s_string = input(" substring to find: ")
try:
    pos = m_string.index(s_string)
    print(f"The substring '{s_string}' is found at position {pos}.")
except ValueError:
    print("Substring was not found.")

#2
grades=[37,89,54]
try:
    average = sum(grades) / len(grades)
    print("Average grade:", average)
except ZeroDivisionError:
    print("List can't be empty")
#3

try:
    numbers = [1, 2, 3, 4, 5]
    print(numbers[7])
except IndexError:
    print("IndexError: Index out of range")
