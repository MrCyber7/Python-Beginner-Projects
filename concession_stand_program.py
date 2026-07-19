# Consession stand program 

print("==== CONSESSION ====")
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzels": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
        
cart = []
total = 0

for items, price in menu.items():
	print(f"{items:10}: ${price:.2f}")
print("--------------------")
while True:
  item = input("Enter food to your cart (q to quit): ").lower()
  if item == "q":
  	break
  elif menu.get(item):
      cart.append(item)
      total += menu.get(item)
  else:
    	print("Item not found!")

print("==== CART ====")   
for total_item in cart:
	print(total_item)
print(f"Total = ${total: .2f}")