import numpy as np
import matplotlib.pyplot as plt
import math as m

x = np.arange(0.1, 10+0.1, 0.1)
y = (1+x)/np.sqrt(x)

plt.plot(x,y, color="red", linewidth=1, linestyle="solid")
plt.show()
