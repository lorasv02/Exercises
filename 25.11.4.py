import matplotlib.pyplot as plt 
list = []

for n in range(0,11):
    list.append(n**2)

plt.plot(list) 
plt.show()