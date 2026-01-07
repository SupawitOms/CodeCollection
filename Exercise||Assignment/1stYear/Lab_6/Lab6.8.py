inp = input("Enter a string : ").split(" ")
list1 = []
ans = ""

for i in inp :
    list1.append(i)

for x in list1:
    chg = x.swapcase()
    ans += (chg + " ")

print("Reverse string output: ",ans)