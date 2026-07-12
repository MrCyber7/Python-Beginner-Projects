# PIN Login system

pin = input("Enter the PIN: ")

#loop
while  not pin == "4321":
  print("Incorrect PIN. Try again.")
  pin = input("Enter the PIN: ")
print("Access Granted!")
