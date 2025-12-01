import math
import numpy 

list = [2, 8, 4, 7, 6]

sum2 = 0

for element in list:
    sum += element

average = sum/len(list)
print (average)

for var in list:
    sum2 += (var - average)**2 

deviation = sum2/(len(list)) 
print (math.sqrt(deviation))

print (numpy.std(list))