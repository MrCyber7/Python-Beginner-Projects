# fibonacci Series

first = 0
second = 1
term = int(input("How many terms?: "))

while term <= 0:
  print("Negative Error!")
  term = int(input("How many terms?: "))

if term == 1:
  print(first)
else:
  print(first)
  print(second)

for series in range(term - 2):
  next = first + second
  first = second
  second = next
  print(next)