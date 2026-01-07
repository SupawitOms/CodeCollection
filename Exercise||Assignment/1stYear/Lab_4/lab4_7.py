
money = int(input("Enter money you have : "))
price = int(input("Enter price of item : "))

tax = (8/100)*price
total = tax + price

print("tax : %d"%tax)
print("Total price : %d"%total)

s_fall = total - money

if money > total :
    print("yes you have enough money to buy")

else :
    print("You have short fall of %d, you cannot buy."%s_fall)
