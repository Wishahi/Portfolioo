from traceback import print_tb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dateutil.parser import parse
import datetime


#Exercise 2
# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# b = a[np.logical_not(np.isnan(a))]
# print(b)

#Exercise 3
# a = np.random.randint(1,100, size=(5, 6))
# print(a)
# maxInRows = np.amax(a, axis=1)
# print('Max value of every Row: ', maxInRows)


#Exercise 4
# series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# print(series)
# seriescount = series.value_counts()
# print(seriescount)

#Exercise 5
# series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# date_series = series.map(lambda x: parse(x))
# # print("Day of month:" + date_series.dt.day.tolist() +  "Week number:" + date_series.dt.weekofyear.tolist() +"Day of year:" + date_series.dt.dayofyear.tolist() + "Day of week:"  + date_series.dt.weekday_name.tolist())
# print("Day of month:")
# print(date_series.dt.day.tolist())
# print("Day of year:")
# print(date_series.dt.year.tolist())
# print("Week number:")
# print(date_series.dt.isocalendar().week.tolist())
# print("Day of week:")
# print(date_series.dt.dayofweek.tolist())

#Exercise 6
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# dataTypeSeries = df.dtypes
# print(dataTypeSeries)
# renameColumn=df.rename(columns = {'Type':'TypeOfCar'}, inplace = True)
# print(df.head)
# missingValues = df.isna().sum()
# print(missingValues)
# highestColumn = df.count().idxmin()
# print(highestColumn)

#Exercise 7
# df.drop(['EngineSize'], inplace=True, axis=1)
# df.drop(df.columns[[18]], axis=1, inplace=True)
# if set(['EngineSize','Length']).issubset(df.columns):
#     print("Yes")
# else:
#     print("No")

#Exercise 8
# df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
#                     'weight': ['high', 'medium', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 9)})

# df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
#                     'kilo': ['high', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 6)})
# out = df1.merge(df2,left_on=('fruit','weight'),right_on=('pazham','kilo'),how='inner',suffixes=('_left','_right')).head(10)
# print(out)

#Exercise 9
# df = pd.DataFrame(["STD,City \tState",
# "33,Kolkata\tWest Bengal",
# "44,Chennai\tTamil Nadu",
# "40,Hyderabad\tTelengana",
# "80,Bangalore\tKarnataka"], columns=['row'])
# out = pd.DataFrame(df.row.str.split(' ',3).tolist(),columns=['STD','City','State'])
# out.drop(index=0,inplace=True)
# print(out)


names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("C:\Users\Leen Wishahi\Desktop\DI-Bootcamp-Stage1\Week-7\ExercisesXP\auto-mpg.data", header=None, names=names, delim_whitespace=True)
#Exercise 10
def scatter_plot():

    plt.scatter(names['displacement'], names['acceleration'])
    plt.xlabel('displacement')
    plt.ylabel('acceleration ')
    plt.grid()
    plt.show() 

#Exercise 11
# def bar_plot():

#     df_mpg.plot(x="Cylinders", y=["model_year", "Height(in cm)"], kind="bar")


# def line_plot():

