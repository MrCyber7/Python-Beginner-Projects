# Reversed Number Pyramid

row = int(input("Enter Rows: "))

while row <= 0:
  print("Negative Error!")
  row = int(input("Enter Rows: "))

for rows in reversed(range(1, row + 1)):
  for spaces in range(row - rows):
    print(" " , end="")
  for column in range(1, rows + 1):
    print(column , end="")
  for opposite in reversed(range(1, column)):
    print(opposite, end="")
  print()
