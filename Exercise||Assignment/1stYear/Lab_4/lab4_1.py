
print("========Welcome to Hi! car Wash========")

service = str(input("Choose your service: W=Wash C=Wash+Vacuum >>> " ))

if service == "W" :
    size = str(input("Enter your car size: \"S\", \"M\", \"L\" : "))

    if size == "S" :
        print("Price = 100")

    elif size == "M" :
        print("Price = 120")

    elif size == "L" :
        print("Price = 140")

    else :
        print("You Enter the wrong car size")

elif service == "C" :
    size = str(input("Enter your car size: \"S\", \"M\", \"L\" : "))

    if size == "S" :
        print("Price = 120")

    elif size == "M" :
        print("Price = 140")

    elif size == "L" :
        print("Price = 160")

    else :
        print("You Enter the wrong car size")

else :
    print("Please Choose Your service")
