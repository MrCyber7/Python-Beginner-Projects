# Password strength checker

print("===== Password Strength Checker =====")
password = input("Enter your password: ")

#loop
while len(password) < 8:
     print("Password too weak to be accepted!")
     password = input("Enter your password: ")

print("Password accepted!")
