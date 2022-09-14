import numpy as np

#2
# print (np.__version__)

# #3
# x = np.zeros(10)
# print(x)

# #4
# y = np.array([100,20,34])
# print(y.itemsize)

# #5
# np.info(np.add)

#6
# x = np.zeros(10)
# x[4] = 1
# print(x)

#7
# x = np.arange(10,50)
# print(x)

#8
# x = np.arange(20)
# x = x[::-1]
# print(x)

#9
# x = np.arange(9).reshape(3,3)
# print(x)

#10
# x = np.nonzero([1,2,0,0,4,0])
# print(x)

#11
# x = np.eye(3)
# print(x)

#12
# x = np.random.random((3,3,3))
# print(x)

#13
# x = np.random.random((10,10))
# print(x)
# xmin, xmax = x.min(), x.max()
# print(xmin, xmax)

#14
# x = np.random.random(30)
# y = x.mean()
# print(y)

#15
# x = np.ones((5,5))
# x[1:-1,1:-1] = 0
# print(x)

#16

#17
# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(0.3 == 3 * 0.1)

#18
# x = np.diag([1, 2, 3, 4, 7])
# print(x)


#19
# x = np.zeros((8,8),dtype=int)
# x[1::2,::2] = 1
# x[::2,1::2] = 1
# print(x)

#20
# x =np.unravel_index(100, (6,7,8,))
# print(x)

#21
# b = np.array([[1, 2], [3, 4]])
# print(np.tile(b,(4,4)))

#22
# x= np.random.random((5,5))
# print(x)
# xmax, xmin = x.max(), x.min()
# x = (x - xmin)/(xmax - xmin)
# # print("After normalization" + x)
# print(x)


#23



