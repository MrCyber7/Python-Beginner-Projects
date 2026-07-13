# BMI calculator

import math

weight = float(input(" Enter your weight(kg): "))
height = float(input(" Entrr your Height(inch): "))

meter = round(height * 0.0254, 3)
bmi = weight / math.pow(meter, 2)

print(f" Your BMI is: {round(bmi, 2)}")

if bmi < 18.5:
	print(" Your BMI is Underweight!")
elif bmi >= 18.5 and bmi <= 24.9:
	print(" Your BMI is Healthy weight!")
elif bmi >= 25.0 and bmi <= 29.9:
	print(" Your BMI is Overweight!")
else:
	print(" Your BMI is Obese!")