# reversed Multiplication Table

print("==== Reversed Multiplication Table ====")
num = int(input("Enter Number: "))
start = int(input("Start from: "))
end = int(input("End at: "))

if num < 0:
  print("Negative Error!")
elif start < 0:
  print("Negative Error!")
elif end < 0:
  print("Negative Error!")
else:
  if end < start:
    for table in reversed(range(end, start + 1)):
      multiply = table * num
      print(f"{num} x {table} = {multiply}")
  else:
    for table in range(start, end + 1):
      multiply = table * num
      print(f"{num} x {table} = {multiply}")
