inp1 = int(input("Input#1 : "))
inp2 = int(input("Input#2 : "))
inp3 = int(input("Input#3 : "))
inp4 = int(input("Input#4 : "))
inp5 = int(input("Input#5 : "))

list1 = [inp1,inp2,inp3,inp4,inp5]
ans = 0

svm = sum(list1)
avg = svm/(len(list1))
mn = min(list1)
mx = max(list1)

opt = int(input("Select the option: 1) Summary, 2) average, 3) min, 4) max ..."))

if opt == 1 :
    print("Your result is %d"%svm)
elif opt == 2 :
    print("Your result is %d"%avg)
elif opt == 3 :
    print("Your result is %d"%mn)
elif opt == 4 :
    print("Your result is %d"%mx)
