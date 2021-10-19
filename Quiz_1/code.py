import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,5,1)
angle = np.linspace(-np.pi , np.pi , 100)

def phase(angle):
    res = []
    for omega in angle:

        if omega > 0:
            res.append( -omega/3 - np.pi/2)
        else:
            res.append(-omega/3 + np.pi/2)

    return res

H = np.array([np.cos(phase(angle)) + 1j*np.sin(phase(angle))])
x = H.real
y = H.imag


plt.plot(n, np.cos(1.5* np.pi*n + np.pi/4) , 'r-')
plt.title("$x[n]$")
plt.grid(True)
plt.show()

plt.plot(x,y , 'ro')
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.title("$H(e^{j\\omega})$")
plt.grid(True)
plt.show()

plt.plot(n,  np.cos(1.5* np.pi*n + np.pi/4 + phase([1.5*np.pi])) , 'r-')
plt.title("$y[n]$")
plt.grid(True)
plt.show()