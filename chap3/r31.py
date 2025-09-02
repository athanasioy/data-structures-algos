import math
import matplotlib.pyplot as plt
import numpy as np

def linear_fn(x:float) -> float:
    return 8*x

def linear_fn_arr(x:np.ndarray) -> np.ndarray:
    return x*8

def log_fn(x:float) -> float:
    return 4*x*math.log2(x)

def log_fn_arr(x:np.ndarray) -> np.ndarray:
    return 4*x*np.log2(x)

def quadratic_fn(x:float) ->float:
    return 2*(x**2)

def quadratic_fn_arr(x:np.ndarray) ->np.ndarray:
    return 2*(x**2)

def cube_fn(x:float) ->float:
    return x**3

def cube_fn_arr(x:np.ndarray) ->np.ndarray:
    return x**3

def exponential_fn(x:float) ->float:
    return 2**x

def exponential_fn_arr(x:np.ndarray) ->np.ndarray:
    return 2**x


x = np.linspace(1,100,200)
y1 = cube_fn_arr(x)
y2 = linear_fn_arr(x)
y3 = quadratic_fn_arr(x)
y4 = exponential_fn_arr(x)
y5 = log_fn_arr(x)
fig, ax = plt.subplots()
ax.loglog(x,y1, label='n^3')
ax.loglog(x,y2, label='8n')
ax.loglog(x,y3, label='2n^2')
ax.loglog(x,y4, label='2^n')
ax.loglog(x,y5, label='4nlogn')
plt.legend()

ax.set_xlabel('n (log scale)')
ax.set_ylabel('f(n) (log scale)')

plt.show()
