# Custom Prime Number Finder

start = int(input("Enter Starting point: "))
end = int(input("Enter Ending point: "))

while start <= 0 or end <= start:
  print("Negative Error!")
  start = int(input("Enter Starting point: "))
  end = int(input("Enter Ending point: "))

for num in range(start, end + 1):
  total = 0
  for factor in range(1, num + 1):
    if num % factor == 0:
     total += 1
  if total == 2:
    print(num)
