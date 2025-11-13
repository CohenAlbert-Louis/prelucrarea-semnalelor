import matplotlib.pyplot as plt
import numpy as np
import csv

N = 18288
N7 = 1001 #dimensiunea esantionului multiplu de 7 (pentru ca fiecare esantion sa inceapa in aceeasi zi saptamanala)

data = np.genfromtxt('Train.csv', delimiter=',',dtype=str)

x = [int(data[i][0]) for i in range(1,N+1)]
d = [data[i][1] for i in range(1,N+1)]
y = [float(data[i][2]) for i in range(1,N+1)]

fig,axs = plt.subplots(N//N7)

for k in range(0,N//N7):
    axs[k].plot(x[k:min((k+1)*N//N7,N)],y[k:min((k+1)*N//N7,N)])

plt.show()