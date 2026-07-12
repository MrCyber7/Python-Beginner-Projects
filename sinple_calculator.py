 import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation(+,-,*,/,**): ")

if operation == "+":
   print(round(num1 + num2, 2))
elif operation == "-":
   print(round(num1 - num2, 2))
elif operation == "*":
   print(round(num1 * num2, 2))
elif operation == "/":
   print(round(num1 / num2, 2))
elif operation == "**":
  print(pow(round(num1, num2, 2)))
else:
  print("Enter correct operation!")