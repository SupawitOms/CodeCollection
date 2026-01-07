import math as m

h = float(input("Enter the pentagon height :"))
a = (h*2)/(m.sqrt(5+(2*m.sqrt(5))))
A = ((a**2)*(m.sqrt(25+(10*m.sqrt(5)))))/4
P = a*5

print("The length for one side of the pentagon is %.4f"%a)
print("The pentagon area and perimeter are %.4f and %.4f"% (A,P))
