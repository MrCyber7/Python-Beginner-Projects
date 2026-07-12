import math

sideA = float(input("Enter Base of the triangle(cm): "))
sideB = float(input("Enter Perpendicular  of the triangle(cm): "))

sideC = math.sqrt(pow(sideA, 2) + pow(sideB, 2))

print(f"The Hypotnuse of the Triangle is: {round(sideC, 2)}cm")