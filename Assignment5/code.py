import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

coeff = np.array([5**0.5 , 1 , 5**0.5])
print(np.roots(coeff))

len = 100
y = np.linspace(-4,4,len)

def parab_gen(y,a):
    x = y**2/a
    return x/4

V = np.array(([5**0.5 , 0],[0,0]))
u = np.array(([0.5,-0.5]))
f = 5**0.5

D_vec,P = LA.eig(V)
D = np.diag(D_vec)


p = P[:,1]

eta = u@p
foc = -(2 * eta)/D_vec[0]

x = parab_gen(y,foc)

cA = np.vstack((u+eta*p,V))
cb = np.vstack((-f,(eta*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()

xStandardparab = np.vstack((y,x))

xActualparab = P@xStandardparab + c[:,np.newaxis]


plt.plot(xActualparab[0,:],xActualparab[1,:],label='$\\sqrt{5}x^2 + x + \\sqrt{5}$',color='r')
plt.plot([i for i in range(-5,5)] , [0 for i in range(-5,5)] , 'k-',label = "x-axis" )
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() 

plt.show()
