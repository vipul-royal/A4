from math import tan, pi
n=int(input("Enter the Number Of Sides="))
side=float(input("Enter the lenght of the side="))
area=n*(side**2)/(4*tan(pi/n))
print("Area Of Polygon is",area)