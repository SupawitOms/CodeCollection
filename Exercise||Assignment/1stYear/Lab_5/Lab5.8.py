print("Menu :")
print("===============")
print("A - Americano (50)")
print("E - Espresso (40)")
print("G - Green tea (60)")
print(" ")

ame = 0
esp = 0
grt = 0
err = 0

inp = str(input("Input: "))
for i in inp:
    if i == "A" :
        ame += 1
    elif i == "E" :
        esp += 1
    elif i == "G" :
        grt += 1
    else :
        err += 0
print("===============")

total_q = ame + esp + grt
total_p = (ame*50)+(esp*40)+(grt*60)
vat = (7/100)*total_p
total_ans = total_p + vat

for i in range(len(inp)) :
    if inp[i] == "A":
        print(i+1,". Americano 50")
    elif inp[i] == "E" :
        print(i+1,". Espresso 40")
    elif inp[i] == "G" :
        print(i+1,". Green Tea 60")

print("===============")
print("Quantity : %d"%total_q)
print("Vat : %.2f"%vat)
print("Total : %.2f"%total_p)
print("Grand total : %.2f"%total_ans)
    
