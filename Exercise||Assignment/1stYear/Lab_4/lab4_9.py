
park = int(input("Input parking time (in minutes) : "))

park_hour = park//60
park_remain = park%60

if park_remain > 15 :
    park_hour += 1

total = park_hour * 20

print("The charge is %d baht"%total)
