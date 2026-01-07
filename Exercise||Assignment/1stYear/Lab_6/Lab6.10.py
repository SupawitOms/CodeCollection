lf = ["Apple","Banana","Orange","Grape","Mango","Kiwi"]

print(lf)

for i in lf:
    fr_c = int(len(i))
    if fr_c <= 5 :
        print("%s is only %d long!"%(i,fr_c))
    elif fr_c >5 :
        print("%s is %d characters or more!"%(i,fr_c))