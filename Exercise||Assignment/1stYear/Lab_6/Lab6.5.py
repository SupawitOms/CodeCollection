grades = []
groups = ["A", "B", "C"]
inp = int(input("how many persons in a group? : "))
for i in groups:
    print("please enter grade from Group", i)
    for j in range(inp):
        grade = float(input("enter grade: "))
        grades.append(grade)

ga = grades[0:inp]
gb = grades[inp:2*inp]
gc = grades[2*inp:]

print("the heighest grade of group A is ",max(ga))
print("the heighest grade of group A is ",max(gb))
print("the heighest grade of group A is ",max(gc))