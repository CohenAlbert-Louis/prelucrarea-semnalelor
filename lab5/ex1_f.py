import numpy as np
import csv
import matplotlib.pyplot as plt

N = 18288

def select_topk(arr,k):
    topk = []
    abs_arr = [abs(elem) for elem in arr]
    sorted_arr = sorted(abs_arr)
    sorted_arr.reverse()
    for i in range(k):
        topk.append(abs_arr.index(sorted_arr[i]))
    return topk

data = np.genfromtxt('Train.csv', delimiter=',',dtype=str)

x = [int(data[i][0]) for i in range(1,N+1)]
d = [data[i][1] for i in range(1,N+1)]
y = [float(data[i][2]) for i in range(1,N+1)]

Y = np.fft.fft(y)
Y = Y[:N//2]

print([e/N for e in select_topk(Y,5)])


