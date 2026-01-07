import random 

ans = ""

s1 = input("Enter string#1 : ")
s2 = input("Enter string#2 : ")
s3 = input("Enter string#3 : ")
s4 = input("Enter string#4 : ")

list1 = [s1,s2,s3,s4]

random.shuffle(list1)

for y in list1 :
    ans += (y + " ")

print("Random order of sentence: ",ans)