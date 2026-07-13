# Positive, Negative and zero counter

# variables
positive = 0
negative = 0
zero = 0

# User Input
num = int(input("How many numbers?: "))

# loop
for enter in range(num):
  if num < 0:
    print("Negative Number!")
    num = int(input("How many numbers?: "))
  else:
    nums = int(input(""))
    if nums < 0:
      negative += 1
    elif nums > 0:
      positive += 1
    else:
      zero += 1

# Output Counter
print(f"Negative = {negative}")
print(f"Positive = {positive}")
print(f"Zero = {zero}")
