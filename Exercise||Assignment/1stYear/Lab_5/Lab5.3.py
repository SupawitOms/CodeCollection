

print("Multiplication table: ")
x = input("Please enter a number between 1 to 25: ")

if x.isnumeric() == True :
    x = int(x)
    if x >= 0 and x <= 25 :
        for i in range(1,13,1) :
            print(x, "x", i, "=", x*i)
    else :
            print("You entered invalid number")
else :
    print("You entered invalid number")

