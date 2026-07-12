# validate user input

username = input("Enter your name: ")

if len(username) < 12 and username.isdigit() == False and username.isalpha == True:
  print(f"Your name is: {username}")
else:
  if len(username) > 12:
    print("Username should NOT exceed 12 Characters!")
  elif username.isdigit:
    print("Username should NOT contain digits!")
  elif not username.isalpha:
    print("Username should NOT have spaces!")