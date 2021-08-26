import numpy as np
import matplotlib.pyplot as plt

def x1(t):
    return np.sin(t)

def x2(t):
    return t

# Let T = 1
def y1 (t): 
    return np.cos(t-1) - np.cos(t)
    
def y2(t):
    return 0.5 * (t**2 - (t-1)**2)
    

def y1plusy2(t):
    return np.cos(t-1) - np.cos(t) + 0.5 * (t**2 - (t-1)**2)

# Plotting input signals
t = np.linspace(-10 , 10, 1000)
plt.plot(t, x1(t) , 'r', label = "$x_1(t) = sin(t)$")
plt.plot(t , x2(t) , 'b', label = "$x_2(t) = t$")
plt.grid(True)
plt.legend(loc = 'upper right')
plt.title("Input signals")
plt.show()

# Plotting output signals
plt.plot(t , y1(t) , 'r', label = "$y_1(t)$")
plt.plot(t , y2(t) , 'b' , label = "$y_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Output Signals: $T = 1$")
plt.show()

# Law of Additivity
plt.plot(t , y1(t) + y2(t) , 'r' , label = "$y_1(t) + y_2(t)$")
plt.plot(t , y1plusy2(t) , 'k--' , label = "System acting on $x_1(t) + x_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Additivity")
plt.show()

# Law of Homogeneity
plt.plot(t , 2 * y1(t)  , 'r' , label = "$2y_1(t)$")
plt.plot(t , 2*(np.cos(t-1) - np.cos(t)) , 'k--' , label = "System acting on $2x_1(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Homogeneity: $k = 2$")
plt.show()

# Time Invariance
# let us introduce a delay of t_0 = 2
plt.plot(t ,  y1(t-2)  , 'r' , label = "$y_1(t-t_0)$")
plt.plot(t , (np.cos(t-3) - np.cos(t-2)) , 'k--' , label = "System acting on $x_1(t-t_0)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Time Invariance")
plt.show()
