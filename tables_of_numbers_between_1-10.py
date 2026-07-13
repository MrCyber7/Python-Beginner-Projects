# tables of Numbers between 1-10

for table in range(1, 11):
  print(f"==== Multiplication Table {table} ====")
  for num in range(1, 11):
    multiply = table * num
    print(f"{table} x {num} = {multiply}")
