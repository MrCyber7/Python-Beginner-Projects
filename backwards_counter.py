# Backwards counter

num = int(input("Enter: "))

while num < 0:
  num = int(input("Enter: "))
for nums in reversed(range(1, num + 1)):
  print(nums)
