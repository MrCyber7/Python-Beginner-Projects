#Multiplication Table

print(" ==== Multiplication Table ====")
num = int(input("Enter a Number: "))

while num < 0:
  print("Enter Positive Number!")
  num = int(input("Enter a Number: "))

for x in range(1, 11):
    multiply = x * num
    print(f"{num} x {x} = {multiply}")