import numpy as np
import matplotlib.pyplot as plt


coeff = np.array([5**0.5 , 1 , 5**0.5])
print(np.roots(coeff))

x = np.linspace(-10,10,10000)
x_axis = np.zeros((10000,))


plt.plot(x , coeff[0]*x**2 + coeff[1]*x + coeff[2] , label = "$\\sqrt{5}x^2 + x + \sqrt{5}$")
plt.plot(x , x_axis , label ="$ y = 0 $")
plt.grid(True)
plt.legend()
plt.ylim(-5,20)
plt.show()
