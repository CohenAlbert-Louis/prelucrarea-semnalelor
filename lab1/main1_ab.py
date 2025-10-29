import matplotlib.pyplot as plt
import numpy as np

fig,axs = plt.subplots(3)
t = np.linspace(0,0.03,20)
axs[0].plot(t,np.cos(520*np.pi*t+np.pi/3))
axs[1].plot(t,np.cos(280*np.pi*t-np.pi/3))
axs[2].plot(t,np.cos(120*np.pi*t+np.pi/3))

plt.show()