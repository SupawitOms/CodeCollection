import random as r

r1 = r.choice([8,9])
r2 = r.choice([6,7])
r3 = r.choice([4,5])
r4 = r.choice([2,3])
r5 = r.choice([0,1])

print("Your OTP is %d%d%d%d%d. This password will be expired within 5 minutes"% (r1,r2,r3,r4,r5))
