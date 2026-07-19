# Shopping cart v3

total_items = []
prices = []
total = 0

while True:
  items = input("Enter Items (q to quit): ")
  if items.lower() == "q":
    break
  else:
    price = float(input("Enter price: $"))
    total_items.append(items)
    prices.append(price)
    total += price

print("==== Shopping Cart ====")
for item in total_items:
  print(item)

for total_price in prices:
  print(total_price)