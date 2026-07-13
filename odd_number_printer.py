# Odd number printer

num = int(input("Enter: "))

while num < 0:
  num = int(input("Enter: "))
for nums in range(1, num + 1):
  if nums % 2 != 0:
    print(nums)
  else:
    continue
