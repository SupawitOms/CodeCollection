n = input("Enter an integer number (n>0) : ")
print("(1) Factorial of n (n!)")
print("(2) Summation of n integers")
ope = input("Select operation: ")

new = 1
new2 = 0

if n.isnumeric() == True :
    n = int(n)
    if ope == "1" :
        for i in range (1,n+1) :
            new = new * (i)
        print("Factorial of n (n!) = %d"%new)
    elif ope == "2" :
        for i in range(n+1) :
            new2 += (i)
        print("Summation of n intergers = %d"%new2)
    else :
        print("N/A Operation!")
else :
    print("N/A Operation!")