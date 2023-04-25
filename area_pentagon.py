# script to calculate the area of a pentagon
import math

r = float(input("Enter the distance from vertex to center of pentagon"))

side = 2*r*math.sin(math.pi/5.0)
A = 3*math.sqrt(3)/2*side**2

print(A)