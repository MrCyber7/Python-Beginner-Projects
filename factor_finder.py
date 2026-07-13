# Factor Finder

num = int(input("Enter Number: "))
Total = 0
print("Factors: ")

while num <= 0:
  print("Negative Error!")
  num = int(input("Enter Number: "))

for factor in range(1, num + 1):
  if num % factor == 0:
    print(factor)
    Total += 1
print(f"Total Factors = {Total}")
