# Simple ATM simulator

print("===== Welcome to Python Bank ATM =====")

name = "Mohammad Ahmed"
acc_number = "987654321"
new_amount = int()
pin = input("Enter the PIN: ")

if pin == "4321":
  print("===== ATM MENU =====")
  print("1. Check Balance")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  menu = input("Choose an option: ")

  if menu == "1":
    print("==================================")
    print(f"Account_Holder: {name}")
    print(f"Account_Number: {acc_number}")
    print(f"Current_Balance: Rs.{new_amount}")
    print("==================================")
  elif menu == "2":
    print("==================================")
    deposit = float(input("Enter amount to deposit: Rs."))
    if deposit > 0:
       new_amount += deposit
       print(f"The previuos Balance was: {new_amount}")
       print(f"The deposited amount is: {deposit}")
       print(f"The New Balance is: {new_amount}")
       print("==================================")
    else:
      print("Invalid deposit amount!")

  elif menu == "3":
    print("==================================")
    withdraw = float(input("Enter amount to withdraw: "))
    if withdraw < 0:
      print("Invalid withdrawal amount!")
      print("==================================")
    elif withdraw > new_amount:
      print("Insufficient balance!")
      print("==================================")
    else:
      new_amount -= withdraw
      print(f"The previuos Balance was: {new_amount}")
      print(f"The Withdrawal amount is: {withdraw}")
      print(f"The New Balance is: {new_amount}")
      print("==================================")
  else:
   print("Invalid option selected!")

else:
  print("Incorrect PIN!")
print("Thank you for using Python Bank ATM.")
print("Have a nice day!")