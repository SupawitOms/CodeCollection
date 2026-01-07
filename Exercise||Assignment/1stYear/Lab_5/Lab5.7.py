Like = 0
Sad = 0
Hea = 0

for _ in range(10) :
    inp = input("Feeling Like (\"L\"), Sad (\"S\"), and Heart(\"H\")? ")
    if inp == "L" :
        Like += 1
    elif inp == "S" :
        Sad += 1
    elif inp == "H" :
        Hea += 1
    else :
        print("Invalid input, accepts only (L/S/H).")

total = Like + Sad + Hea
p_li = (Like/total)*100
p_sa = (Sad/total)*100
p_he = (Hea/total)*100

print("============")
print("Total is %d"%total)
print("============")
print("Like : %d (%.2f%%)"% (Like,p_li))
print("Sad : %d (%.2f%%)"% (Sad,p_sa))
print("Heart : %d (%.2f%%)"% (Hea,p_he))