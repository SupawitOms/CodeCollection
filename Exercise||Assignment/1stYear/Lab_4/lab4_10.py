
print("Welcome to Income Tax Computation Program")

income = float(input("\nPlease enter your income (THB): "))

tax = 0
if income > 100000 :
    tax += (35000*0.05)+(50000*0.075)+((income-100000)*0.1)
elif income >= 50001 :
    tax += (35000*0.05)+((income-50000)*0.075)
elif income >= 15001 :
    tax += (income-15000)*0.05
    
if income >= 0:
    print("\nTax expense = %.2f"%tax)

    cal = income - tax
    
    print("Your net income after tax = %.2f"%cal)
else :
    print("\nYou are in debt!")

