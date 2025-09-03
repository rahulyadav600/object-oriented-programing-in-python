import matplotlib.pyplot as plt
import numpy as np 

x = np.array([23, 23, 45, 34, 45])
y = x**2

plt.plot(x, y)
plt.savefig('1.png')
plt.show()
