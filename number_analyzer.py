# Number Analyzer

total = 0
total_sum = 0
reverse = 0
total_digit = 0
nums = 0
sum_of_digit = 0

num = int(input(" Enter a positive number: "))

while num < 0:
 print(" Negative Error!")
 num = int(input(" Enter a positive number: "))

print(" ==== Number Analizer ====")
if num % 2 == 0:
  print(" Even Number!")
else:
  print(" Odd Number!")

for factor in range(1, num + 1):
  if num % factor == 0:
    total += 1
    total_sum += factor
if total == 2:
  print(" Prime Number!")
else:
  print(" Not a Prime Number!")
if total_sum - num == num:
  print(" Perfect Number!")
else: 
  print(" Not a Perfect Number!")
nums = num

while num != 0:
	digit = num % 10
	num = num // 10
	sum_of_digit += digit	
	reverse = reverse * 10 + digit
	total_digit += 1
print(f" Total Digits = {total_digit}")
print(f" Reversed Number = {reverse}")
if reverse == nums:
	print(" Palindrome!")
else:
	print(" Not a Palindrome!")

print(f" Sum Of Digits = {sum_of_digit}")