def myRange(FirstVal,UpperBound,StepSize) :
    for i in range(FirstVal,UpperBound,StepSize) :
        listt.append(i)
    print(listt)
listt = []

FirstVal = int(input("Enter the first number: "))
UpperBound = int(input("Enter the upper bound: "))
StepSize = int(input("Enter the step: "))

myRange(FirstVal,UpperBound,StepSize)