import numpy as np
import csv
import matplotlib.pyplot as plt

N = 18288

data = np.genfromtxt('Train.csv', delimiter=',',dtype=str)

x = [int(data[i][0]) for i in range(1,N+1)]
d = [data[i][1] for i in range(1,N+1)]
y = [float(data[i][2]) for i in range(1,N+1)]

Y = np.fft.fft(y)

Y = Y[50:18238] # taiem capetele si peste ca sa eliminam componenta continua si orice artifact conex acestuia
Y = [0 for i in range(50)]+list(Y)+[0 for i in range(50)]

#Verificare
#yabs = [] 

#for ye in Y:
#    yabs.append(abs(ye/N))

#plt.plot([i/N for i in range(0,18288)],yabs)
#plt.show()

y2 = np.fft.ifft(Y)

fig,axs = plt.subplots(2)

axs[0].set_title('Semnalul fara componenta continua')
axs[0].plot([i for i in range(0,N)],abs(y2.real))
axs[1].set_title('Semnalul original')
axs[1].plot([i for i in range(0,N)],y)

plt.show()