import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#numpy
# lst = [2, 4, 6, 8, 13, 2020]
# second = [0, 5, 33, -750, 2,8]
# numpy_arr = np.array(lst,second)
# # numpy_arrarray([   2,    4,    6,    8,   13, 2020])
# # print(numpy_arr)
# minElement=np.min(numpy_arr)
# print(minElement)
# stdDev = np.std(numpy_arr)
# print(stdDev)
# prod = np.product(numpy_arr)
# print(prod)
# # dotarr=np.dot(numpy_arr)
# # print(dotarr)
# subtarray = numpy_arr - 4
# print(subtarray)

#pandas
# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# # df = df.iloc[50]
# # print(df)
# df.groupby('species').apply(np.mean)
# print(df)

# x = [1, 2, 3, 4]
# y = [2, 20, 35, 6]
# plt.plot(x, y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('first graph')
# plt.show()

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# plt.plot(data.id, data["sepal_length"], "r--") 
# plt.show()

#scatter
# plt.scatter(data['sepal_length'], data['petal_length'])
# plt.xlabel('sepal_length (cm)')
# plt.ylabel('petal_length (cm)')
# plt.grid() 
# plt.show()

# histogram
setosa_data = data[data.species == 'setosa']
versicolor_data = data[data.species == 'versicolor']
virginica_data = data[data.species == 'virginica']

fig, ax=plt.subplots(1,3,figsize=(13, 5))


ax[0].hist(setosa_data.petal_length, color='g', label = 'setosa')
ax[1].hist(versicolor_data.petal_length, color='r', label = 'versicolor')
ax[2].hist(virginica_data.petal_length, color='b', label = 'virginica')

ax[0].legend()
ax[1].legend()
ax[2].legend()
ax[0].set_ylabel('Frequency')
ax[1].set_ylabel('Frequency')
ax[2].set_ylabel('Frequency')
ax[0].set_xlabel('petal length (cm)')
ax[1].set_xlabel('petal length (cm)')
ax[2].set_xlabel('petal length (cm)')

plt.show()


# x = np.random.randint(0,76,(50,2))
# y = np.random.randint(0,76,(50,2))
# plt.scatter(x, y)
# plt.xlabel('rand x')
# plt.ylabel('rand y')
# plt.grid() 
# plt.show()

