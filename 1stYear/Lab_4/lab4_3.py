day = int(input("Input number of days: "))
hour = int(input("Input number of hours: "))

print("Please select a choice:")
print("1-to calculate the total number of seconds or \n 2- to calculate the total number of minutes")

choice = int(input("Enter your selected choice: "))
minute = ((day*24)+hour)*60
second = minute*60


if choice == 1:
  print("The total number of seconds are %d"%second)
else:
  print("The total number of minutes are %d"%minute)
