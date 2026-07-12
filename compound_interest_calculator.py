# python compund interest calculator

#variables assign
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the Interest Rate: "))
time = float(input("Enter the time in year: "))

#if user puts negative values then it restarts!
while  not principal > 0 or not rate > 0 or not time >0:
   print("The values are incorret!")
   principal = float(input("Enter the principal amount: "))
   rate = float(input("Enter the Interest Rate: "))
   time = float(input("Enter the time in year: "))

amount = principal*(pow(1 + rate/100, time))
compound = amount - principal

print(f"The principal amount is: ${principal: .2f}")
print(f"The compund amount is: ${amount: .2f}")
print(f"The compound interest is: ${compound:.2f}")
