# Even/Odd Counter

even = 0
odd = 0

num = int(input("Enter: "))

while num < 0:
  print("Negative Number!")
  num = int(input("Enter: "))
for x in range(1, num + 1):
  if x % 2 == 0:
     even += 1
  else:
    odd += 1
print(f"Even Numbers: {even}")
print(f"Odd Numbers: {odd}")