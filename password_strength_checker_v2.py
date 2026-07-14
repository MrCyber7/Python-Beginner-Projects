# Password Strength Checker V2

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
has_length = False

special ="!@#$%&*^_-?/;~"
strength = 0

while password == "":
  print("Enter Something!")
  password = input("Enter password: ")

for character in password:
    if character.isupper():
      has_upper = True
    if character.islower():
      has_lower = True
    if character.isdigit():
      has_digit = True
    if character in special:
      has_special = True
if len(password) >= 8:
  has_length = True

if has_upper:
  strength += 1
if has_lower:
  strength += 1
if has_digit:
  strength += 1
if has_special:
  strength += 1
if has_length:
  strength += 1

if strength <= 3:
  print("WEAK!")
elif strength == 4:
  print("MEDIUM!")
else:
  print("STRONG!")
