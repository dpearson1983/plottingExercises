import sys
import math
import numpy as np
import matplotlib.pyplot as plt

a = "not set"; b = "not set"; A = "not set"; lam = "not set"; phi = "not set"; sigma = "not set"
N = "not set"
for i in range(1,len(sys.argv)):
    if (sys.argv[i] == "-a"):
        a = float(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-b"):
        b = float(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-A"):
        A = float(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-lam"):
        lam = float(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-phi"):
        phi = float(sys.argv[i + 1])*math.pi/180.0
        i += 1
    elif (sys.argv[i] == "-N"):
        N = int(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-sigma"):
        sigma = float(sys.argv[i + 1])
        i += 1

if (a == "not set"):
    a = float(input("Enter low value of x range: "))
if (b == "not set"):
    b = float(input("Enter high value of x range: "))
if (A == "not set"):
    A = float(input("Enter amplitude: "))
if (lam == "not set"):
    lam = float(input("Enter wavelength: "))
if (phi == "not set"):
    phi = float(input("Enter phase angle in degrees: "))*math.pi/180.0
if (sigma == "not set"):
    sigma = float(input("Enter variance as percentage of amplitude: "))
if (N == "not set"):
    N = int(input("Enter number of data points: "))

x = np.linspace(a, b, N)
k = 2*math.pi/lam
y = A*np.sin(k*x + phi)
y = np.random.normal(y,sigma*A,N)

plt.errorbar(x,y,yerr=A*sigma,fmt="o")
plt.savefig("sinusoidPlot2.pdf")

outFile = open("sinusoidPlot2.txt", "w")
for i in range(0,N):
    outFile.write(str(x[i]) + " " + str(y[i]) + " " + str(sigma*A) + "\n")
outFile.close()