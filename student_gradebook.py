# Student GradeBook

names = []
marks = []
grades = []
nums = int(input("How many students?: "))
total = 0
avg = 0

while nums <= 0:
  print("Negative Error!")
  nums = int(input("How many students?: "))

for num in range(nums):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))

    names.append(name)
    marks.append(mark)

    if mark >= 90 and mark <= 100:
      grades.append("A")
    elif mark >= 80 and mark < 90:
      grades.append("B")
    elif mark >= 70 and mark < 80:
      grades.append("C")
    elif mark >= 60 and mark < 70:
      grades.append("D")
    else:
      grades.append("F")

highest = marks[0]
lowest = marks[0]
for mark in marks:
    total += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
avg = total / nums

print("==== GRADEBOOK ====")
for index in range(len(names)):
  print(f"{names[index]}    {marks[index]}    {grades[index]}")
print(f"Average marks = {avg: .2f}")