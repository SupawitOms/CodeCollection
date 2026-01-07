inp = input("Enter a comma-seperated list : ").split(",")

list1 = []

if int(len(inp)) >= 3 :
    for i in inp:
        for j in inp:
            for k in inp:
                # print(1)
                if i != j and i != k and k != j and sorted([i,j,k]) not in list1:
                    print(i,j,k)
                    list1.append([i,j,k])
