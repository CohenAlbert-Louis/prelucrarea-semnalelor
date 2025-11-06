import numpy as np
import matplotlib.pyplot as plt

def signal(n):
    return np.sin(2*np.pi*3*n)

def signal_alias(n):
    return np.sin(2*np.pi*73*n) #k=1

def signal_alias2(n):
    return np.sin(-2*np.pi*67*n) #k=-1

t = [i/70 for i in range(70)]

fig,axs = plt.subplots(3)

axs[0].set_title('original signal')
axs[1].set_title('alias 1')
axs[2].set_title('alias 2')

axs[0].plot(t,[signal(i) for i in t])
axs[1].plot(t,[signal_alias(i) for i in t]) #esantionare la 70Hz
axs[2].plot(t,[signal_alias2(i) for i in t]) #esantionare la 70Hz

plt.figure()
plt.title('overlap')

ol = [signal(i) if (abs(signal(i)-signal_alias(i))<1e-10 or abs(signal(i)-signal_alias2(i))<1e-10) else 0 for i in t]

plt.stem(t,ol) #suprapuneri

plt.show()