
print("===================================")

x = float(input("Input x = "))
y = float(input("Input y = "))
x_1 = 0
x_2 = 2
x_3 = 1
y_1 = 0
y_2 = 0
y_3 = 2


alpha = ((y_2-y_3)*(x-x_3)+(x_3-x_2)*(y-y_3)) / ((y_2-y_3)*(x_1-x_3)+(x_3-x_2)*(y_1-y_3))
beta = ((y_3-y_1)*(x-x_3)+(x_1-x_3)*(y-y_3)) / ((y_2-y_3)*(x_1-x_3)+(x_3-x_2)*(y_1-y_3))
gamma = 1 - alpha - beta

if alpha > 0 and beta>0 and gamma>0:
    print("Point [x,y] inside polygon")

else :
    print("Point [x,y] outside polygon")
