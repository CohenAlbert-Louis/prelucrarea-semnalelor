import matplotlib.pyplot as plt
import numpy as np

t1 = np.linspace(0,4,1600)
t2 = np.linspace(0,3,2400)
t3 = np.linspace(0,1,240)
t4 = np.linspace(0,1,300)

def myfunc(x):
    return np.sqrt(x)

ra = np.array(np.random.rand(128,128))
mya = np.vectorize(myfunc)(np.array(np.random.rand(128,128)))

fig,axs=plt.subplots(4)
axs[0].plot(t1,np.sin(2*np.pi*t1+np.pi/3))
axs[1].plot(t2,np.sin(np.pi*t2-np.pi/2))
axs[2].plot(t3,np.mod(t3,0.2))
axs[3].plot(t4,np.sign(t4-0.3)*np.sign(0.5-t4))

plt.figure()
plt.imshow(ra)
plt.figure()
plt.imshow(mya)

plt.show()