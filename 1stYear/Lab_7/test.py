while True :
    num = int(input("Enter an integer number : "))

    if num < 1 or num > 10 :
        print("Please enter a number between 1 and 10.")
    else :
        #top
        for i in range(1,num+1) :
            for j in range(1, i+1) :
                print(j, end=" ")
            print()

        #bottom
        for i in range(num-1,0,-1) :
            for j in range(1,i+1) :
                print(j, end=" ")
            print()
        
