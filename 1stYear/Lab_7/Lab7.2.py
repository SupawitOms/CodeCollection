li = []
i = ""

while i != "exit" :
    i = str(input("Input: Enter a word: "))
    if i != "exit" :
        i = i.capitalize()
        li.append(i)

print(li)