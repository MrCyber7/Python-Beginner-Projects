# Reverse Number

num = int(input("Enter the number: "))
reverse = 0

while num <= 0:
  print("Negative Error!")
  num = int(input("Enter the number: "))
number = num
print("==== Result ====")

while num != 0:
  digit = num % 10
  num = num // 10
  reverse = reverse * 10 + digit
print(f"Reversed Number = {reverse}")
if reverse == number:
  print(f"{number} is a Palindrome")
else:
  print(f"{number} is NOT a Palindrome")