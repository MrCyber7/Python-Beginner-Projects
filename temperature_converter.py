# temparature converter

temperature = float(input("Enter the temperature: "))
unit = input("Celcius or Farenheit (C or F): ")

if unit == "C" or unit == "c":
	temperature = (9 * temperature) / 5 + 32
	print(f"The temperature in Fahrenheit is: {round(temperature, 2)}°F")
elif unit == "F" or unit == "f":
	temperature = (temperature - 32) * 5 / 9
	print(f"The temperature in Celcius is: {round(temperature, 2)}°C")
else:
	print(f"{unit} is incorrect!")