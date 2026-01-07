inp = ""

while inp != "X" :
    inp = input("Enter an integer number ('X' to exit): ")
    if inp.isnumeric() :
        if int(inp) % 2 != 0 :
            for i in range(0,inp) :
                i = int(i)
                inp = int(inp)
                print("x"*i + "."*(inp-2) + "x"*i)