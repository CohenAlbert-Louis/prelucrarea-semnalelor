import numpy as np
import matplotlib.pyplot as plt

def rectangular(lb,ub):
    return lambda x: 1 if x>=lb and x<=ub else 0

def autoconv(x,n):
    res = 0
    for i in range(n):
        res += x[i]*x[n-1-i]
    return res

def signal(t):
    return np.sin(2*np.pi*t)+np.cos(3*np.pi*t)

sample_n = [i*0.001 for i in range(-1000,1000)]
sampled_signal = signal #signal or rectangular

fig,axs = plt.subplots(4)

samples = [sampled_signal(t) for t in sample_n]
ac_samples = [autoconv(samples,t) for t in range(len(samples))]
ac_2_samples = [autoconv(ac_samples,t) for t in range(len(ac_samples))]
ac_3_samples = [autoconv(ac_2_samples,t) for t in range(len(ac_2_samples))]

axs[0].plot(sample_n,samples) #x
axs[1].plot(sample_n,ac_samples) #x2
axs[2].plot(sample_n,ac_2_samples) #x4
axs[3].plot(sample_n,ac_3_samples) #x8

plt.show()