x = 0

while x == 0 :
    print(" ")
    print("===== MAIN MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    print(" ")

    ope = input("Select an operation (1-3) : ")

    if ope == "1" or ope == "2":     
        num1,num2 = input("Enter two numbers: ").split(" ")

        sum = int(num1) + int(num2)
        sub = int(num1) - int(num2)

        if ope == "1" :
            print("%s + %s = %d"%(num1,num2,sum))
        elif ope == "2" :
            print("%s - %s = %d"%(num1,num2,sub))
    
    elif ope == "3" :
        x += 1

print("Bye!!!")
