import numpy as np

data = np.loadtxt("sales.tsv")

branch = data[0:6,0:1]

sum_1 = np.sum(data[0:1,1:4])
sum_2 = np.sum(data[1:2,1:4])
sum_3 = np.sum(data[2:3,1:4])
sum_4 = np.sum(data[3:4,1:4])
sum_5 = np.sum(data[4:5,1:4])

result = np.array([sum_1,sum_2,sum_3,sum_4,sum_5])
order = np.argsort(result)

for i in reversed(order):
    print("%d : %d "%(branch[i], result[i]))