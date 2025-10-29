import matplotlib.pyplot as plt
import numpy as np

def signal(omega):
    return np.sin(20*np.pi*omega)-2*np.sin(30*np.pi*omega)+np.sin(60*np.pi*omega)

def fourier_transform(func, omega, N):
    result = 0
    for n in range(N):
        result += func(n/N) * np.exp(-2j * np.pi * omega * n / N)
    return result

t = np.linspace(0,80,80)
plt.plot(t,np.abs(fourier_transform(signal, t, 1000)))

plt.show()