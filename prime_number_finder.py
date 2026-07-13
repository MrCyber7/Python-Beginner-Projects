# Prime Number Finder

num = int(input("Enter Number: "))
Total = 0

while num <= 0:
  print("Negative Error!")
  num = int(input("Enter Number: "))

for factor in range(1, num + 1):
  if num % factor == 0:
    Total += 1
if Total == 2:
    print(f"{num} Prime Number")
else:
    print(f"{num} Not a Prime Number")
print(f"Total Factors = {Total}")
