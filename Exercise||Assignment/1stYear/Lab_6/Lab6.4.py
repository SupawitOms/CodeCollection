nl = ["Sasawat","Pisit","Thanapong","Pished","Nut","Amon"]
for i in range(10):
    print(nl)

    inp = str(input("Please enter a student's name that you want to delete (q = exit) : "))

    if inp == "q" :
        break

    print("You will remove '%s' from this class."%inp)
    cf = str(input("Please type (Confirm 'y', Cancel 'n') : "))

    if cf == "y" :
        nl.remove(inp)