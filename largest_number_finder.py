# Largest Number Finder

#User input
num = int(input("How many numbers?: "))
first = int(input("Enter first number: "))
largest = first
entered = 0
while entered + 1 != num :
  if num < 0:
    print("Negative Number!")
    num = int(input("How many numbers?: "))
  else:
    entered += 1
    nums = int(input(""))
    if nums > largest:
      largest = nums
print(f"largest Number = {largest} ")

