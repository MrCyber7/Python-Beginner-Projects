# Armstrong number

total = 0
num = int(input("Enter a 3 digit number: "))
digit = 0

while num < 100 or num > 999:
  print("3 digits ONLY!")
  num = int(input("Enter a 3 digit number: "))
number = num
print("==== Result ====")

while num != 0:
  digit = num % 10
  num = num // 10
  total += digit ** 3
print(f"Total = {total}")
if total == number:
  print(f"{total} is an Armstrong Number!")
else:
  print(f"{total} is NOT an Armstrong Number!")