# Sum and Average Calculator

enter = int(input("How many numbers?: "))
total = 0
avg = 0

if enter < 0:
    print("Negative Error!")
else:
    for entered in range(enter):
      num = float(input(""))
      while num < 0:
        print("Negative Error!")
        num = float(input(""))
      total += num
    avg = total / enter
    print("==== Result ====")
    print(f"Sum = {total}")
    print(f"Average = {round(avg,2)}")
