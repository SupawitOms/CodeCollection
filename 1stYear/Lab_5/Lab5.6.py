
for i in range(5) :
    num = int(input("enter a number between 1 and 20: "))
    if num >= 1 and num <= 20 :
        if num % 2 == 0 :
            print("%d is an even number"%num)
        else :
            print("%d is an odd number"%num)
    else :
        print("number is invalid")