
withd = int(input("Please specific amount of money you would like to withdraw: "))

five_hund = withd//500
one_hund = (withd%500)//100
five_ty = ((withd%500)%100)//50
two_c = (((withd%500)%100)%50)//2
one_c = ((((withd%500)%100)%50)%2)//1

print("we may give you: ")
print("%d bill(s) of 500 bath"%five_hund)
print("%d bill(s) of 100 bath"%one_hund)
print("%d bill(s) of 50 bath"%five_ty)
print("%d bill(s) of 2 bath"%two_c)
print("%d bill(s) of 1 bath"%one_c)
