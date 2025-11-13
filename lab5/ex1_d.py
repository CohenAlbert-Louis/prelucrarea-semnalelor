import numpy as np
import matplotlib.pyplot as plt
import csv

N = 18288

data = np.genfromtxt('Train.csv', delimiter=',',dtype=str)

x = [int(data[i][0]) for i in range(1,N+1)]
d = [data[i][1] for i in range(1,N+1)]
y = [float(data[i][2]) for i in range(1,N+1)]

Y = np.fft.fft(y)
Y = Y[:N//2]

plt.plot([i/N for i in range(0,N//2)],np.abs(Y/N))
plt.show()