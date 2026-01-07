inp = str(input("Enter dd/mm/yyyy : "))

if len(inp) != 8:
    print("Please enter 8 digits!!")
else : 
    dat = int(inp[:2])
    mon = int(inp[2:4])
    year = int(inp[4:])

    if dat in range(32) :
        if mon in range(13) :
            print("Date = ",dat)
            print("Month = ",mon)
            print("Year = ",year-543)
        else :
            print("Error! There're 12 months")
    else :
            print("Error! There're 31 days")
    
        
            
        
        

