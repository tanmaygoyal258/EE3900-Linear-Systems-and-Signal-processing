# Plotting fourier transforms
T = 0.00004
f_0 = 10000
t = np.arange(0.0, 0.001, 0.00001)
x   = np.cos(2*np.pi*f_0*t)
y = np.sin(2*np.pi*f_0*t) - np.sin(2*np.pi*f_0*(t-T))
fourier_input = np.fft.fft(x)
fourier_output = np.fft.fft(y)
fourier_input=np.fft.fft(x)
freq=np.fft.fftfreq(fourier_input.shape[0], d=1/1e5)

plt.plot(freq , np.abs(fourier_input) , label = "Fourier Transform of $x(t) = cos 2 \\pi f_0 t$")
plt.plot(freq , np.abs(fourier_output) , label = "Fourier Transform of $y(t) = \\int_{t-T}^t x(t)\\,dt$")
plt.legend()
plt.grid(True)
plt.show()
