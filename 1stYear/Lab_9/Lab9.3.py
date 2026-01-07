def SumOut():
    print("The summation  is %d"%sum(xList))

def MinOut():
    print("The minimum is %d"%min(xList))

def MaxOut():
    print("The maximum is %d"%max(xList))

xList = []

def UserInput() :
    while True :
        inp = input("Enter an input: ")
        
        if inp != "Done" :
        
            if inp.isnumeric():
                inp = int(inp)
                if inp >= 0 :
                    xList.append(inp)
                
                else :
                    print("Error")
                    break
            else :
                print("Error")
                break
        else :
            print("")
            SumOut()
            MinOut()
            MaxOut()

try:
    UserInput()
    
except:
    print("Error")