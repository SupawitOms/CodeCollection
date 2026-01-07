import matplotlib.pyplot as plt
import numpy as np
import math as m

c_wid = float(input("Enter the width of the cube : "))
con_wid = float(input("Enter the width of the container : "))
con_hei = float(input("Enter the height of the container : "))
con_dep = float(input("Enter the depth of the container : "))

total_w = con_wid//c_wid
total_h = con_hei//c_wid
total_d = con_dep//c_wid

total_total = total_w * total_h * total_d

print("The number of cubes that can fit into the container is %d"% total_total)
