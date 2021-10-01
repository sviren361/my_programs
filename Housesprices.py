import numpy as np
data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
mean=np.mean(data)
std=np.std(data)
x1=int(mean-std)
x2=int(mean+std)
y=(data>x1) & (data<x2)
out=data[y]
print((len(out)/len(data))*100)