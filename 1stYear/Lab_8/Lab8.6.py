dictt = {}

while True:

    inp = input("Input (DONE = exit): ")

    if inp == "DONE" :
        break
    else :
        id, score = inp.split(" ")    
        
        if id.isalpha() :
            print("Invalid input")
        
        id, score = int(id), int(score)
        
        if id <= 0 or score <= 0:
            print("Invalid input")
        else :
            if int(id) in dictt:
                if dictt[int(id)] < int(score):
                    dictt[int(id)] = int(score)
            else:
                dictt[int(id)] = int(score)

for key in sorted(dictt, key=dictt.get, reverse=True) :
    print(key, dictt[key])