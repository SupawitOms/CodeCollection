price = int

def SeatType():
    global inp
    seat = ["P","D","H"]
    inp = ""
    while True :
        inp = input("Select the seat type (P or D or H): ")

        if inp in seat :
            break
        else :
            print("Wrong seat type! Please select again.")

def MovieType():
    global mov
    movie = ["1","2"]
    mov = ""
    while True:
        mov = input("Select the movie type (1 or 2): ")

        if mov in movie:
            break
        else:
            print("Wrong movie type! Please select again.")

def TicketPrice():
    print("")

    if inp == "P" :
        if mov == "1" :
            price = 100
        else :
            price = 120
    elif inp == "D" :
        if mov == "1" :
            price = 140
        else :
            price = 200
    else :
        if mov == "1" :
            price = 400
        else :
            price = 500

    print("The ticket price is %d"%price)

SeatType()
MovieType()
TicketPrice()