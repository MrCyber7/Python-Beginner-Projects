print("--------------------")
print("   Shopping Cart    ")
print("--------------------")

item = input("Enter the item you purchased: ")
quantity = int(input("Enter the quantity of your item: "))
price = float(input("Enter the price of the item:$"))

total = quantity * price

print("--------------------")
print("       Total        ")
print("--------------------")

print(f"The total amount for {quantity} {item} for {price} each is: ${total}")
