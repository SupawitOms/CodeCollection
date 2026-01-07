import math as m

def SquareArea():
    s_a = s*s 

    print("The area of the square is %.2f"%s_a)

def CircleArea():
    c_a = m.pi*(r*r)

    print("The area of the circle is %.2f"%c_a)

choice = ["s","c"]

inp = input("Do you want to find the area of a square (s) or a circle(c)?: ")

if inp in choice :
    if inp == "s" :
        s = float(input("Enter the length: "))
        print("")
        SquareArea()
    else :
        r = float(input("Enter the radius: "))
        print("")
        CircleArea()
else :
    print("")
    print("Wrong Input")