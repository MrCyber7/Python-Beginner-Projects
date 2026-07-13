# Opposite Rigjt Angle triangle

rows = int(input(" Enter Rows: "))


for row in range(1, rows + 1):
    for spaces in range(rows - row):
        print("  ", end="")

    for stars in range(1, row + 1):
        print("* ", end="")

    print()
	    