import numpy as np

col = []

def loopinp():
    for i in range(inp):
        for j in range(inp):
            inp2 = int(input("Input element at row %d column %d : "%(i+1,j+1)))
            col.append(inp2)


inp = int(input("Input size of matrix : "))
loopinp()

mat = np.reshape(col,(inp,inp))
print(mat)

print("Determinant = %.1f"%np.linalg.det(mat))

print("Inverse matrix = \n",np.linalg.inv(mat))