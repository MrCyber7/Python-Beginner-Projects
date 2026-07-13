# weight converter

weight = float(input("Enter the weight: "))
unit = input("Pounds or Kilograms?(L/K): ")

if unit == "L" or unit == "l":
	result = round(weight * 2.205, 2)
	print(f"Your weight in Kilograms is: {result}Kg")
elif unit == "K" or unit == "k":
	result = round(weight / 2.205, 2)
	print(f"Your weight in Pounds is: {result}L")
else:
	print(f"{unit} is incorrect! ")