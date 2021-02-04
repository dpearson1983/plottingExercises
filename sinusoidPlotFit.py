import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x = np.array([])
y = np.array([])
sig = np.array([])

inFile = open("sinusoidPlot.txt", "r")
for line in inFile:
    X, Y, S = line.split(" ")
    x = np.append(x, float(X))
    y = np.append(y, float(Y))
    sig = np.append(sig, float(S))
inFile.close()

def f(x, A, k, phi):
    return A*np.sin(k*x + phi)

def residual(p, x, y):
    return (y - f(x, *p))/sig

p0 = [3.0, 2.5, 0.2]
popt, pcov = optimize.leastsq(residual, p0, args=(x,y))

print("Best fitting parameter values:")
print(popt)

m = len(x)
xn = np.linspace(x[0], x[m-1], 1000)
yn = f(xn, *popt)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.errorbar(x,y,yerr=sig,fmt="o")
plt.plot(xn,yn)
plt.show()