num = int(input("enter no. of lines: "))

if num >= 1 :
    for i in range(1,num,1) :
        if i % 2 == 0 :
            print("*"*i)
        else :
            print("-"*i)
        # print("")
else :
    print("Error")