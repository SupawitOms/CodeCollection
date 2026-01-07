odd , even = 0,0

for _ in range(5) :
    num = int(input("enter a number "))
    if num % 2 == 0 :
        even += 1
    else :
        odd += 1

print("there were %d even numbers"%even)
print("there were %d even numbers"%odd)