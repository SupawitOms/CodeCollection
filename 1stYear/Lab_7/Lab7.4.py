print("'''")
inp = int(input("Enter an integer number : "))
i = 0
x = inp - 2

print("x "*inp)

while i < inp :
    if x != 0 :
        print("x " + "  "*x + "x")
        i += 1
    else :
        break

print("x "*inp)