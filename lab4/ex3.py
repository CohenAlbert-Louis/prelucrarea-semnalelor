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

axs[0].set_title('original signal (70Hz)')
axs[1].set_title('alias 1 (70Hz)')
axs[2].set_title('alias 2 (70Hz)')

axs[0].plot(t,[signal(i) for i in t])
axs[1].plot(t,[signal_alias(i) for i in t]) #esantionare la 70Hz
axs[2].plot(t,[signal_alias2(i) for i in t]) #esantionare la 70Hz

fig2,axs2 = plt.subplots(3)

axs2[0].set_title('original signal (100Hz)')
axs2[1].set_title('alias 1 (100Hz)')
axs2[2].set_title('alias 2 (100Hz)')

t2 = [i/100 for i in range(100)]

axs2[0].plot(t2,[signal(i) for i in t2])
axs2[1].plot(t2,[signal_alias(i) for i in t2])
axs2[2].plot(t2,[signal_alias2(i) for i in t2])

plt.show()