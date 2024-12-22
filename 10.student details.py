name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")

maths = float(input("Enter maths marks: "))
science = float(input("Enter science marks: "))
english = float(input("Enter english marks: "))

average = (maths + science + english) / 3

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\nStudent Details:")
print("Name:", name)
print("Roll Number:", roll_number)
print("Maths Marks:", maths)
print("Science Marks:", science)
print("English Marks:", english)
print("Average Marks:", average)
print("Grade:",grade)