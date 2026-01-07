import math as m

def cira():
    cir_a = m.pi*(x*x)

    return cir_a

def sqa():
    sq_a = x*x

    return sq_a

x = input("Input a positive number: ")

if x.isalpha() :
    print("Wrong input")

else :
    x = float(x)

    if x < 0 :
        print("Wrong input")
        
    else :
        

        print("The area of the circle is %.2f"%cira())
        print("The area of the square is %.2f"%sqa())

