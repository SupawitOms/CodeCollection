inp = input("Enter a comma-seperated list : ").split(",")

list1 = []

for x in inp:
    list1.append(x)

for i in list1:
    for j in list1:
        for k in list1:
            if i != j and j != k and k != i :
                print(i,j,k)