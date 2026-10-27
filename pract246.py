import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,6)


plt.plot(x,x**2)
plt.plot(x,x**3)
plt.plot(x,2*x)
plt.legend()
plt.show()

