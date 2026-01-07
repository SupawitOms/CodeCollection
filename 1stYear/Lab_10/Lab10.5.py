import numpy as np
def distance(x,y):
    d = np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2+(x[2]-y[2])**2)
    return d


p = []
for i in range(1,4):
    inp = input("Input Coordinated of P%d: "%i).split()
    p.append([int(inp[0]), int(inp[1]), int(inp[2])])

p1 = p[0]
p2 = p[1]
p3 = p[2]

d1 = distance(p1,p2)
d2 = distance(p1,p3)
d3= distance(p2,p3)

d = max([d1,d2,d3])

print("The longest distance is %.2f"%d)