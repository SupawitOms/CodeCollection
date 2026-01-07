import numpy as np

data = np.loadtxt("grade.tsv")
print("Student ID  \t GPA")
for i in data:
    sid = (i[0])
    grades = (i[1]*3+i[2]*2+i[3]+i[4]*3+i[5]*3+i[6]*3)/(3+2+1+3+3+3)
    print("%d \t %.2f"%(sid, grades))