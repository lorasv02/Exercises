list = [1, 4, 9]


sum = 0

if len(list) == 0:
    print ("None")
    exit ()

for current in list:
    sum += current

average = sum/len(list)
print (average)



    