import numpy as np
import matplotlib.pyplot as plt
import time

def my_dft(signal_disc): #de optimizat
    N = len(signal_disc)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, signal_disc)

def my_fft(signal_disc):
    N = len(signal_disc)
    if N <= 1:
        return signal_disc
    even = my_fft(signal_disc[0::2])
    odd = my_fft(signal_disc[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def fft_time(signal_disc):
    start_time = time.time()
    my_fft(signal_disc)
    return time.time() - start_time

def dft_time(signal_disc):
    start_time = time.time()
    my_dft(signal_disc)
    return time.time() - start_time

def np_fft_time(signal_disc):
    start_time = time.time()
    np.fft.fft(signal_disc)
    return time.time() - start_time

def signal(n):
    return np.sin(2*np.pi*30*n+np.pi)+0.5*np.sin(2*np.pi*20*n)

discrete_128 = [signal(60/128*i) for i in range(128)]
discrete_256 = [signal(60/256*i) for i in range(256)]
discrete_512 = [signal(60/512*i) for i in range(512)]
discrete_1024 = [signal(60/1024*i) for i in range(1024)]
discrete_2048 = [signal(60/2048*i) for i in range(2048)]
discrete_4096 = [signal(60/4096*i) for i in range(4096)]
discrete_8192 = [signal(60/8192*i) for i in range(8192)]

discrete_all = [discrete_128, discrete_256, discrete_512, discrete_1024, discrete_2048, discrete_4096, discrete_8192]

fig,axs = plt.subplots(3)

axs[0].set_title('DFT time')
axs[1].set_title('FFT time')
axs[2].set_title('np FFT time')

for ax in axs:
    ax.set_xlabel('Sample number')
    ax.set_ylabel('Time')

axs[0].set_yscale('log')
axs[1].set_yscale('log')
axs[2].set_yscale('log')

axs[0].plot([128,256,512,1024,2048,4096,8192], [dft_time(d) for d in discrete_all])
axs[1].plot([128,256,512,1024,2048,4096,8192], [fft_time(d) for d in discrete_all])
axs[2].plot([128,256,512,1024,2048,4096,8192], [np_fft_time(d) for d in discrete_all])

plt.show()