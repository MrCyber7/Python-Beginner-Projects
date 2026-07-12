# rectangle

rows = int(input("Enter the rows for the Rectangle: "))
column = int(input("Enter the column for the Rectangle: "))
symbol = input("Enter a symbol: ")
for x in range(rows):
  for y in range(column):
    print(symbol, end="")
  print()