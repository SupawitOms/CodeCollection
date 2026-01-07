dictt = {}

while True:

    inp = input("Input (DONE = exit): ")

    if inp == "DONE" :
        break
    else :
        id, score = inp.split(" ")   
        
        if id.isalpha() :
            print("Invalid input")
        elif id in dictt.keys() :
            print("Duplicated ID")
        else :
            dictt[int(id)] = int(score)

for key in sorted(dictt, key=dictt.get, reverse=True) :
    print(key, dictt[key])
