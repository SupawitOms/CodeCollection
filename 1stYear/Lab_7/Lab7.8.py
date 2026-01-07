inp = int
even = 0
odd = 0

while inp != 0 :
    inp = int(input("Enter an integer (0 to exit): "))
    if inp != 0 :
        if inp % 2 == 0 :
            even += 1
        elif inp %2 != 0 :
            odd += 1

print("----------------------------------")
print("The number of even integers is ",even)
print("The number of odd intergers is ",odd)