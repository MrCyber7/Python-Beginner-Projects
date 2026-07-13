#Student grade report

name = input("Enter the name of the student: ")
roll_no = int(input("Enter the roll number of the student: "))

eng = float(input("English marks: "))
math = float(input("Math marks: "))
science = float(input("Science marks: "))
comp = float(input("Computer marks: "))
isl = float(input("Islamiat marks: "))	

total = eng + math + science + comp + isl
percentage = round((total / 500) * 100, 2)

if percentage >= 90 and percentage <= 100:
	grade = "A*"
elif percentage >= 80 and percentage < 90:
	grade = "A"
elif percentage >= 70 and percentage < 80:
	grade = "B"
elif percentage >= 60 and percentage < 70:
	grade = "C"
elif percentage >= 50 and percentage < 60:
	grade = "D"
elif percentage < 50 and percentage >= 0:
	grade = "F"
else:
	print("Enter correct marks")

print("-------------------")
print("     Report Card       ")
print("-------------------")

print(f"student name: {name}")
print(f"Roll number: {roll_no}")
print("-------------------")
print(f" English marks:   {eng}")
print(f" Math marks:     {math}")
print(f" Science marks:  {science}")
print(f" Computer marks: {comp}")
print(f" Islamiat marks:  {isl}")
print("-------------------")
print(f"Your Total marks out of 500 are: {total}")
print(f"Your Percentage is: {percentage}%")
print(f"Your Grade is: {grade}")
print("Passed" if percentage >=50 and percentage <= 100 and percentage >= 0 else "Failed")
