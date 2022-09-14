import random
import numpy as np
# np.random.randint(1,100, (40,40))

def two_array(M,N):
    if M < 50 and N < 40:
        arr = [[random.randint(1,100) for i in range(N)] for x in range(M)]
        return arr


array = two_array(30,30)
# len1 = len(array)
# print(len1)    
row =array[2]
print(row)
for i in array:
  print(i[2]) 


for i in range(len(array[-1])):
    array[-1][i] = 7
    print(array[-1])

    

