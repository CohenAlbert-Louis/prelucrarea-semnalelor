import numpy as np
import csv
import matplotlib.pyplot as plt

print("Frecventa de esantionare este: ",1/18288," Hz")
print(18288/24," zile intregi de esantioane")

N = 18288

data = np.genfromtxt('Train.csv', delimiter=',',dtype=str)

x = [int(data[i][0]) for i in range(1,N+1)]
d = [data[i][1] for i in range(1,N+1)]
y = [float(data[i][2]) for i in range(1,N+1)]

Y = np.fft.fft(y)
Y = Y[:N//2]

max_val = -1000000
max_freq = 0
curr_pos = 0

for ly in Y:
    max_val = ly if ly>=max_val else max_val
    max_freq = curr_pos if ly==max_val else max_freq
    curr_pos+=1 

print("Frecventa maxima: ",max_freq/N," cu modulul: ",max_val)