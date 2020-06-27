from math import sin,pi
r=float(input("Enter the Radius Of the Circle="))
a=float(input("Enter the angle of the Circle(to 180)"))
area=((r*r)/2)*((pi/180)*a-sin(a))
print("Area of Segment Of the Circle=",area)