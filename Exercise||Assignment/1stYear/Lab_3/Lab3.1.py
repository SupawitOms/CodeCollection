import matplotlib.pyplot as plt
import numpy as np
import math as m

x = np.arange(-3*(m.pi),3*(m.pi),0.1)
y1 = np.sin(x)
y2 = np.sin(x + 0.5)
y3 = np.sin(x +1)
y4 = np.sin(x + 1.5)

plt.plot(x,y1, color="pink", linewidth=1.5, linestyle="dotted")
plt.plot(x,y2, color="GREEN", linewidth=1.5, linestyle="dashed")
plt.plot(x,y3, color="orange", linewidth=1.5, linestyle="dashdot")
plt.plot(x,y4, color="pink", linewidth=1.5, linestyle="solid")
plt.show()
