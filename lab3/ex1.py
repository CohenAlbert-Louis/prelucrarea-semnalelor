import matplotlib.pyplot as plt
import numpy as np

def signal(omega):
    return np.sin(2*np.pi*omega)+0.5*np.sin(4*np.pi*omega)+0.25*np.sin(6*np.pi*omega)

def fourier_matrix(fx,N):
    F = np.zeros((N,N),dtype=complex)
    for n in range(N):
        for k in range(N):
            F[n,k] = np.exp(-2j*np.pi*k*fx(n)/N)
    return F

fig,axs = plt.subplots(2)
axs[0].set_title('Real')
axs[1].set_title('Imag')

fm = fourier_matrix(signal,8)
t = np.linspace(0,2*np.pi,8)

fm = fm / np.sqrt(8)  # normalizare
for i in range(0,8):
    re = np.real(fm[:,i])
    im = np.imag(fm[:,i])
    axs[0].plot(t,re)
    axs[1].plot(t,im)

plt.show()