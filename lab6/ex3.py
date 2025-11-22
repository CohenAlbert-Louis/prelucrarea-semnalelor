import numpy as np
import matplotlib.pyplot as plt

def gen_polynomial(N):
    n_arr = [10*np.random.rand() for i in range(N+1)]
    s_arr = [1 if np.random.rand()>0.5 else -1 for _ in range(N+1)] #sign array
    def pol(x):
        res = 0
        for i in range(N+1):
            res += s_arr[i]*n_arr[i]*(x**i)
        return res
    return pol 

sample_n = [i*0.001 for i in range (-5000,5000)]

fig,axs = plt.subplots(4)

poly_1 = gen_polynomial(3)
poly_2 = gen_polynomial(3)

axs[0].plot(sample_n,[poly_1(t) for t in sample_n])
axs[1].plot(sample_n,[poly_2(t) for t in sample_n])
axs[2].plot(sample_n,[poly_1(t)*poly_2(t) for t in sample_n])

fpoly_1 = np.fft.fft([poly_1(t) for t in sample_n])
fpoly_2 = np.fft.fft([poly_2(t) for t in sample_n])
fpoly_conv = np.convolve(fpoly_1,fpoly_2)

fft_prod = np.fft.ifft(fpoly_conv,n=len(sample_n))

axs[3].plot(sample_n,[fft_prod[i].real for i in range(len(sample_n))])

plt.show()

