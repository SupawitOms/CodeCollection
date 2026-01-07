sum = 0

for x in range(5) :
    order = x+1
    num = int(input("Enter an integer #%d : "%order))
    sum += num

print("The summation is %d"%sum)