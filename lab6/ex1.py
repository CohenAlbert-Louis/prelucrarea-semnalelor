import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt

def sinc_2(B,x):
    return np.sinc(B*x)**2

def reconstruct_signal(sampled_signal,Ts,t):
    summ = 0
    for n in range(len(sampled_signal)):
       summ += sampled_signal[n]*np.sinc((t-n*Ts)/Ts)
    return summ

Ts = 6
B = 0.5

sample_n_1Hz = [i for i in range(-3,3)]
sample_n_1_5Hz = [i*0.333 for i in range(-9,9)]
sample_n_2Hz = [i*0.5 for i in range(-6,6)]
sample_n_4Hz = [i*0.25 for i in range(-12,12)]
sample_n_40Hz = [i*0.025 for i in range(-120,120)] #reference

fig,axs = plt.subplots(5)

sinc_2_samples_1Hz = [sinc_2(B,sn) for sn in sample_n_1Hz]
sinc_2_samples_1_5Hz = [sinc_2(B,sn) for sn in sample_n_1_5Hz]
sinc_2_samples_2Hz = [sinc_2(B,sn) for sn in sample_n_2Hz]
sinc_2_samples_4Hz = [sinc_2(B,sn) for sn in sample_n_4Hz]
sinc_2_samples_40Hz = [sinc_2(B,sn) for sn in sample_n_40Hz]

axs[0].plot(sample_n_1Hz,sinc_2_samples_1Hz)
axs[1].plot(sample_n_1_5Hz,sinc_2_samples_1_5Hz)
axs[2].plot(sample_n_2Hz,sinc_2_samples_2Hz)
axs[3].plot(sample_n_4Hz,sinc_2_samples_4Hz)
axs[4].plot(sample_n_40Hz,sinc_2_samples_40Hz)

axs[0].plot(sample_n_1Hz,[reconstruct_signal(sinc_2_samples_1Hz,Ts,t) for t in sample_n_1Hz])
axs[1].plot(sample_n_1_5Hz,[reconstruct_signal(sinc_2_samples_1_5Hz,Ts,t) for t in sample_n_1_5Hz])
axs[2].plot(sample_n_2Hz,[reconstruct_signal(sinc_2_samples_2Hz,Ts,t) for t in sample_n_2Hz])
axs[3].plot(sample_n_4Hz,[reconstruct_signal(sinc_2_samples_4Hz,Ts,t) for t in sample_n_4Hz])
axs[4].plot(sample_n_40Hz,[reconstruct_signal(sinc_2_samples_40Hz,Ts,t) for t in sample_n_40Hz])

plt.show()
