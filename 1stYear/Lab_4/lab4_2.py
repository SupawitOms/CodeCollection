print("Fever symtoms Advisor Program")
temp = float(input("Check your body temperature in F = "))

if temp >= 100.4 :
  print("You got a fever.")

  med = int(input("Choose your treatment : 1 = medication 2 = no medication >>> "))

  if med == 1:
    print("Take tylenol every 4 hours are needed")
  elif med == 2:
    print("Taking a bath in lukewarm water or get the cool pack")
  else:
    print("You choose wrong choice")

else:
  print("You are fine.")
