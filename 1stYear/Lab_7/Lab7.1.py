li = []
i = ""

while i != "exit" :
    i = str(input("Input: Enter a word: "))
    if i != "exit" :
        if i.endswith("y") :
            i = i.replace("y", "ily")
            li.append(i)
        else :
            li.append(i)

print(li)