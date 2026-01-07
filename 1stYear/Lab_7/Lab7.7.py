print("===================")
print("Cashier Program")
print("===================")
print("")
inp = 0
list1 = []

while inp != -1 :
    inp = float(input("Enter item price or -1 when finished: "))
    if inp > 0 :
        list1.append(inp)

print("")
print("Total puchase amount is ", sum(list1))
print("")

pay = int(input("Your payment: "))
print("")

print("You bought ", len(list1),"items today.")
print("Your change is ", pay - sum(list1),"baht.")