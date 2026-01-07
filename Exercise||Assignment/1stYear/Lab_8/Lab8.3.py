inp1 = input("Input sequence1: ").split(" ")
inp2 = input("Input sequence2: ").split(" ")
seq1 = set()
seq2 = set()

for i in inp1 :
    if i.isdigit() :
        seq1.add(i)

for x in inp2 :
    if x.isdigit() :
        seq2.add(x)

if seq1 == seq2 :
    print("Output : Same set")
else :
    print("Output : Different set")