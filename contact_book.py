# Contact Book

contact_book = {"ahmed": "09384753654"}

while True:
print("==== CONTACT BOOK ====")
print("1. Add Contact""\n""2. Search Contact""\n""3. Delete Contact""\n""4. Show All Contacts""\n""5. Quit")
print("======================")

 choice = int(input("Enter: "))
if choice == 1:
   name = input("Enter name: ")
   phone_number = input("Enter Phone Number: ")
   if name in contact_book or phone_number in contact_book.values():
    print("Already in contact book!")
   else:
    contact_book.update({name: phone_number})
elif choice == 2:
    name = input("Enter name: ")
    if name in contact_book:
      print(f"{name}: {contact_book[name]}")
    else:
      print("Name NOT Found!")
elif choice == 3:
    name = input("Enter name: ")
    if name in contact_book:
      contact_book.pop(name)
    else:
      print("Name NOT Found!")
elif choice == 4:
    print("==== CONTACT BOOK ====")
    for key,values in contact_book.items():
      print(f"{key}: {values}")
elif choice == 5:
    break
else:
  print("Invalid Choice!")