

print("Welcome to pizza online ordering")
print("please input \"y\" if you want to order, otherwise input \"n\" ")

pizza = str(input("pizza? (price_359) : "))
chick = str(input("chicken? (price_3 pieces for 199) : "))
pasta = str(input("pasta? (price_99 : )"))
salad = str(input("salad? (price_99 : )"))
coke = str(input("coke? (price_550 ml for 25) : "))

total = 0

if pizza == "y":
    total += 359
if chick == "y":
    total += 199
if pasta == "y":
    total += 99
if salad == "y":
    total += 99
if coke == "y":
    total += 25

print("total price is %d \nthanks"%total)
