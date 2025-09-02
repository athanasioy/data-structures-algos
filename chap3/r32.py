import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,20,30)

y1 = np.log2(x)*8*x
y2 = 2*x**2
fig, ax = plt.subplots()

ax.plot(x,y1, label='$8xlogx$')
ax.plot(x,y2, label='$2x^2$')
# n0=16
# define g(n)=n-4logn
# g(n) is monotonically increasing for n>4
# g(n) one of root is 16
# thus n0=16 such that 2x^2 > 8logn, for every x>n0
plt.legend()
plt.show()

