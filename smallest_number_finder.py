# smallest Number Finder

num = int(input("How many numbers?: "))
first = int(input("Enter First Number: "))
smallest = first

for enter in range(num - 1):
  if num < 0:
    print("Negative Number!")
    num = int(input("How many numbers?: "))
  else:
    nums = int(input(""))
    if nums < smallest:
      smallest = nums
print(f"Smallest Number = {smallest}")
