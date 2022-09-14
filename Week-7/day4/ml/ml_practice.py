#iris predicitions through machine learning

import matplotlib
import pandas as pd
import numpy as np
#import sklearn
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

##all depp learning started with perceptron
# print(df.describe())
# print(df.info())
#data that we pass it has to be numerical 
#we have to decide what we want to predict 

setosa_flowers = df.loc[df['species'] == 'setosa']
versicolor_flowers =df.loc[df['species'] == 'versicolor']
viriginica_flowers =df.loc[df['species'] == 'virginica']

# virginica_flowers = df.loc[df['species'] == 'virginica']
# print(len(virginica_flowers))

# virginica_flowers[['sepal_length', 'sepal_width']].plot(x = 'sepal_length', y= 'sepal_width', kind='line')
# plt.show()
# virginica_flowers[['sepal_length', 'sepal_width']].plot(x = 'sepal_length', y= 'sepal_width', kind='scatter')
# plt.show()



#sepal
vg_sl = viriginica_flowers['sepal_length']
vg_sw = viriginica_flowers['sepal_width']

s_sl = setosa_flowers['sepal_length']
s_sw = setosa_flowers['sepal_width']

ver_sl = versicolor_flowers['sepal_length']
ver_sw = versicolor_flowers['sepal_width']

# plt.scatter([vg_sl], [vg_sw], color='red', label='Viriginca')
# plt.scatter([s_sl], [s_sw], color='green', label='Setosa')
# plt.scatter([ver_sl], [ver_sw], color='orange', label='Versicolor')

# plt.xlabel('Sepal Length')
# plt.ylabel('Sepal Width')
# # plt.hist()
# plt.legend(loc = 'upper right')
# plt.show()





#petal
vg_pl = viriginica_flowers['petal_length']
vg_pw = viriginica_flowers['petal_width']

s_pl = setosa_flowers['petal_length']
s_pw = setosa_flowers['petal_width']

ver_pl = versicolor_flowers['petal_length']
ver_pw = versicolor_flowers['petal_width']

# plt.scatter([vg_pl], [vg_pw], color='red', label='Viriginca')
# plt.scatter([s_pl], [s_pw], color='green', label='Setosa')
# plt.scatter([ver_pl], [ver_pw], color='orange', label='Versicolor')

# plt.xlabel('Petal Length')
# plt.ylabel('Petal Width')
# # plt.hist()
# plt.legend(loc = 'upper right')
# plt.show()


#PREPROCESS

#extract what we want to predict

#kinds of y :
#numerical continous (543.56, 665,89, 5775.90)
#categorical (1,2,3) (couple of classes)

y = df['species']
print(y.head())

#Species is categorical and nominal
#use one hot encoding
# nominal is when you dont have an order
# #ordinal is when you have an order
# 

#shows which flower is a species
print(pd.get_dummies(y))

y = LabelBinarizer().fit_transform(y)
# print(y)

##define x - the data for training 

# X = df.loc[:, df.columns!='species']
# print(x.head())

#transfrom x 

# X = X.to_numpy()
# print(type(X))
# print(X)

# x[:5]
# print(x)

#training and testing
X_train,X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state=42)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)


knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train,y_train)
# print(knn_model.predict(X_test))
# print(y_test)
#how accurate
# print(knn_model.score(X_test, y_test))




 #keras.com
 #sktlearn scikit.
 #kaggle categorical 
 #y =survived 
#  titanic_df.drop(columns = ['Cabin'])
# pd.get_dummies( tianic_df['Sex'])
# pd.get_dummies(titanic_df['Embarked'])







clf = MLPClassifier(solver='lbfgs',
 alpha=5, 
 hidden_layer_sizes=(40,4), 
 max_iter=8, 
 random_state =1,
 learning_rate_init=0.2,
 verbose=10)

clf.fit(X_train, y_train)

# print(clf.predict(X_test))
