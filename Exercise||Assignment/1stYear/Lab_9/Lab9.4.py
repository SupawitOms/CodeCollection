def UserInput():
    global ww , hh
    ww = float(input("Input your weight (kilogram): "))
    hh = float(input("Input your height (meter): "))

def FindBMI(hh,ww) :
    UserBMI = ww / (hh*hh)
    global MyBMI
    MyBMI = UserBMI

def ShowBMI(MyBMI) :
    print("The user BMI is %.2f"%MyBMI)

UserInput()
FindBMI(hh,ww)
ShowBMI(MyBMI)