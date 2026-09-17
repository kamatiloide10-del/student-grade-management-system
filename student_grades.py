# Student Grade Management System

student_name = input("Enter student name: ")

mark1 = float(input("Enter mark for Test 1: "))
mark2 = float(input("Enter mark for Test 2: "))
mark3 = float(input("Enter mark for Test 3: "))

average = (mark1 + mark2 + mark3) / 3

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent:", student_name)
print("Average:", round(average, 2))
print("Grade:", grade)
