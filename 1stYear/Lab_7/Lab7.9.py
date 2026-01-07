inp = 0
list1 = []

while inp != -1 :
    inp = int(input("Enter an integer (-1 to exit): "))
    if inp != -1 :
        list1.append(inp)

print("The sum of %d number(s) is %d."%(len(list1),len(list1)))