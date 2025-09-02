import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,30,30)

y1 = 40*x**2
y2 = 2*x**3

fig, ax = plt.subplots()

ax.plot(x,y1, label='$40x^2$')
ax.plot(x,y2, label='$2x^3$')
# n0=20, such that for every x>n0
# 40x^2 < 3x^3
plt.legend()
plt.show()
