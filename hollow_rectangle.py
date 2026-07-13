# Hollow Rectangle

rows = int(input("Enter the rows for the Rectangle: "))
column = int(input("Enter the column for the Rectangle: "))
symbol = input("Enter a symbol: ")
for x in range(rows):
  for y in range(column):
    if x == 0 or y == column - 1 or x == rows - 1 or y == 0:
      print(symbol, end="")
    else:
      print(" ", end="")

  print()
