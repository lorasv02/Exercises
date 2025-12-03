import numpy 

list = [1, 5.1, 9, 6, 3] 
list.sort() 

gone_index = len(list)//2 
if len(list) % 2 == 0: 
    print ((list[gone_index]+list[gone_index-1])/2)  
else: 
    print (list[gone_index])  
 
print(numpy.median(list)) 











