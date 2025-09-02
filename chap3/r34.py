import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0,1000,500)

fig, ax = plt.subplots()

ax.plot(x,x)

plt.show()

fig,ax2 = plt.subplots()

ax2.loglog(x,x)

plt.show()
