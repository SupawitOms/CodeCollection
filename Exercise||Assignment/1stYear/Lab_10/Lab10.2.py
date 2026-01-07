import numpy as np

col = []
axis = ["x","y","z"]

inv = True

def linear() :
    for i in range(12) :
        inp = int(input("Input C%d: "%(i+1)))
        col.append(inp)

    mat = np.reshape(col,(3,4))
    x = mat[:,:3]
    y = mat[:,3]
    
    global yc , inv_x
    yc = np.reshape(y,(3,1))
    if np.linalg.det(x)!=0:
        inv_x = np.linalg.inv(x)

    else:
        global inv
        inv = False
    
linear()

if inv:
    ans = np.matmul(inv_x,yc)

    print("Solution:")

    for x in range(3) :
        print("%s = %.2f"%(axis[x],ans[x]))
else:
    print("\nUnable to find a solution")