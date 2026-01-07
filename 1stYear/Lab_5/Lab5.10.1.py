inp = input("Input : ")
err = False

for i in inp :
    if len(inp) != 9 or (i != "X" and i != "O" and i != ".") :
        err = True

if err == True :
    print("Error")
else :
    for i, x in enumerate(inp) :
        print("|%s"%x, end ="")
        if (i+1)%3 == 0:
            print("|")
            print("-"*7)