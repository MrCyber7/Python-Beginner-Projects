# Even/Odd number sum

even = 0
odd = 0
print("==== Even/Odd Number Sum ==== ")
num = int(input("Enter: "))

while num < 0:
  num = int(input("Enter: "))

for nums in range(1, num + 1):
    if nums % 2 == 0:
      even += nums
    else:
      odd += nums

print(f"Sum of Even: {even}")
print(f"Sum of Odd: {odd}")