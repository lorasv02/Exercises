import os
file = open ("test_3.txt", 'w')

file.write("namess")

os._exit(1)
print("this will not be printed")
file.close()
