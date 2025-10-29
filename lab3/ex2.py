import matplotlib.pyplot as plt
import numpy as np

def signal(omega):
    return np.sin(2*np.pi*omega)+np.sin(2*np.pi*omega+np.pi/4)

fig, axs = plt.subplots(2)
axs[0].set_xlabel('Timp (esantioane)')
axs[0].set_ylabel('Amplitudine')
axs[1].set_xlabel('Real')
axs[1].set_ylabel('Imaginar')

tsamples = np.linspace(0,1000,1000)
t = np.linspace(0,1,1000)

axs[0].plot(tsamples,signal(t))
axs[1].scatter(np.real(signal(t)*np.exp(-2*np.pi*1j*t)),np.imag(signal(t)*np.exp(-2*np.pi*1j*t)),s=1)

fig2,axs2 = plt.subplots(4)

for i in range(0,4):
    axs2[i].set_xlabel('Real')
    axs2[i].set_ylabel('Imaginar')
    
axs2[0].set_title('omega = 1')
axs2[1].set_title('omega = 2')
axs2[2].set_title('omega = 5')
axs2[3].set_title('omega = 7')

axs2[0].scatter(np.real(signal(t)*np.exp(-2*np.pi*1j*1*t)),np.imag(signal(t)*np.exp(-2*np.pi*1j*1*t)),s=1)
axs2[1].scatter(np.real(signal(t)*np.exp(-2*np.pi*1j*2*t)),np.imag(signal(t)*np.exp(-2*np.pi*1j*2*t)),s=1)
axs2[2].scatter(np.real(signal(t)*np.exp(-2*np.pi*1j*5*t)),np.imag(signal(t)*np.exp(-2*np.pi*1j*5*t)),s=1)
axs2[3].scatter(np.real(signal(t)*np.exp(-2*np.pi*1j*7*t)),np.imag(signal(t)*np.exp(-2*np.pi*1j*7*t)),s=1)

plt.show()