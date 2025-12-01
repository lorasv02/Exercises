import math 
import matplotlib.pyplot as plt 
y = []
x = []

for n in range(0,2001):
    x.append((n-1000)*0.01)
    y.append(math.exp(x[-1]))


plt.plot(x,y) 
plt.show()


