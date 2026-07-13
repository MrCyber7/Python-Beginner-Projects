# Reversed Right angle triangle

rows = int(input(" Enter Rows: "))

for row in reversed(range(1, rows + 1)):
	for columns in range(1, row+1):
	  print(" *", end="")
	print()