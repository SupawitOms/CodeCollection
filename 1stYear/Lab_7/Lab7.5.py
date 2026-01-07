inp = 0

while inp < 1 or inp > 10 :
    inp = int(input("Enter an integer number : "))

    if inp < 1 or inp > 10 :
        print("1 - 10 !!!!")
    
    else :
        for x in range(inp) :
            for y in range(x+1) :
                print(y+1, end=" ")
            print(" ")
        
        for i in range(inp-1, 0, -1) :
            for j in range(1,i+1) :
                print(j, end=" ")
            print(" ")