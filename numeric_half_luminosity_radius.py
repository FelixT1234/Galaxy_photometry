import numpy as np
from scipy.optimize import fsolve

def f(r, h):
        return (h*np.log(2*(r/h+1))-r) # define the function f, so that f(r, h) = 0

h_list = np.arange(0.01, 20, 0.01) # list with values for h

# result should be the approximation: r = value*h
value_list = []
for h in h_list:
    initial_guess = h
    r = fsolve(f, initial_guess, args=(h))[0] # r is the numeric value, so that for a fixed h: f(r,h) = 0
    value_list.append(r/h) # follows from approximation: value = r/h

print(np.mean(value_list)) # prints the arithmetic mean
