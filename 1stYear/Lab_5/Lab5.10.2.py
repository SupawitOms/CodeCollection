inp = "X.X......"
print("-"*7)

for i in range(len(inp)):
    print("|%s"%inp[i], end="")
    if (i+1)%3==0:
        print("|")
        print("-"*7)