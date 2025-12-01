import math 
import matplotlib.pyplot as plt 
a = 1
b = 2
z = 0.3
y = []
x = []

for n in range(0,2001):
    x.append((n-1000)*0.01)
    y.append(a*math.exp(-z*(x[-1]-b)**2))


plt.plot(x,y) 
plt.show()