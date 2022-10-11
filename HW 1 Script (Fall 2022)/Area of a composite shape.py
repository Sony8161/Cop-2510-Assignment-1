# Duong Lam U68618275 Area of a composite shape
''' This program allows you to input two diagonal lengths of a composite shape, and the radius of a circle in order to
find the area of the composite shape.
'''


import math


diagon1 =int(input("Enter the first diagonal length:"))

diagon2 =int(input("Enter the second diagonal length:"))

radius = int(input("Enter the radius of the circle:"))

radius2 =(radius * radius)

pi =math.pi

kite =round(((diagon1 * diagon2)/2),3)


circle = (pi * radius2)


shaded_area = round((kite - circle),3)


print(f"The shaded area is {shaded_area} square units.")


