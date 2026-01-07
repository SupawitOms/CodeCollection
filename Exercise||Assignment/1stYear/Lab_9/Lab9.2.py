def leftro():
    list_leftro = listt[n:] + listt[:n]
    print("The left-rotated list: ", list_leftro)

def rightro():
    list_rightro = listt[-n:] + listt[:-n]
    print("The right-rotated list ", list_rightro)

listt = input("Enter 5 inputs: ").split(" ")

n = input("Enter an integer number of rotations (0-4): ")

if n.isdigit():
    n = int(n)
    
    if n >= 0 and n<=4 :
        leftro()
        rightro()

    else :
        print("Error!")
else :
    print("Error!")