def TriArea(h,b):
    tri_a = (1/2)*h*b

    return tri_a


h = float(input("Enter the height (h): "))
b = float(input("Enter the base (b): "))

print("The area of the triangle is",TriArea(h,b))