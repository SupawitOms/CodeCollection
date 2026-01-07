inp1 = input("Input sequence1: ").split(" ")
inp2 = input("Input sequence2: ").split(" ")

seq1 = set()
seq2 = set()

for i in inp1 :
    if i.isnumeric() :
        seq1.add(i)

for i in inp2 :
    if i.isnumeric() :
        seq2.add(i)


if seq1:
    for x in seq1 :
        if x in seq2 == True :
            print("Output:", x in seq2)
            break
        else :
            print("Output:", x in seq2)
            break
else:
    print("Output: False")
