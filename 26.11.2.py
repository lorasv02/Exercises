import math 
import matplotlib.pyplot as plt 
y = []
x = []

for n in range(0,11):
    x.append(n)
    y.append(math.exp(-math.pi*n**2))


plt.plot(x,y) 
plt.show()


