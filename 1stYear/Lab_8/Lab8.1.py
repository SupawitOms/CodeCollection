dictt = {}

inp = input("Input: ").split(" ")

for i in inp :
    i = i.lower()
    if i in dictt :
        dictt[i] += 1
    else :
        dictt[i] = 1

print("Output: ")

for k,v in dictt.items():
    if v == max(dictt.values()):
        print(k, "=",v)