inp = int(input("Enter an integer number : "))
i = 0
x = inp - 2

print("o "*inp)
while i < inp:
    if x != 0 :
        x -= 1
        print("o " + "  "*i + "x "*(x+1) + "o")
        i += 1
    else :
        break
print("o "*inp)