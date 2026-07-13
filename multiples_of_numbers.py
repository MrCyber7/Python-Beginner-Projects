# Multiples of numbers

# User input
num = int(input("Enter the Starting Number: "))
limit = int(input("Enter the limit Number: "))

#loop
for value in range(num, limit + 1):
  if value % num == 0:
     print(value)
