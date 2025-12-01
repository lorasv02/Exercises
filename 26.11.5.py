import math 
import matplotlib.pyplot as plt 
a = 1
b = 2
z = 0.3

y_1 = []
y_2 = []
y_3 = []
x = []

for n in range(0,2001):
    x.append((n-1000)*0.01)
    y_1.append(a*math.exp(-z*(x[-1]-b)**2))

a = 3
b = -2
z = 0.1


for n in range(0,2001):
    y_2.append(a*math.exp(-z*(x[n]-b)**2))



for n in range(0,2001):
    y_3.append(y_1[n]+y_2[n])


plt.plot(x,y_1) 
plt.plot(x,y_2) 
plt.plot(x,y_3) 
plt.show()