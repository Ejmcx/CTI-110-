#Elijah Mcarthur
10/4/26
#the program will cacluate the diameter,circumference, and area of a circle given the radius

#import the math module to use the value of pi
import math

#Get the radius from the user
radius = float(input("Enter the radius of the circle: "))
print()

#calculate diameter
diameter = 2 * radius

#display diamter with 1 decimal place
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate circumference
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}\n")

#calcute the area
area = math.pi * radius ** 2

#Display area with 3 decimal places
print(f"The area of the circle is {area:.3f}\n")

