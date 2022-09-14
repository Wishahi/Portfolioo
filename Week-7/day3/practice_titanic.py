import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

#prints columns headers
# print(titanic_df.columns.values)

#first 5 rows
# print(titanic_df.head())

#describes the statics for the numerical problems
# print(titanic_df.describe())

#shows the non-null values
#do you drop the null values?
# print(titanic_df.info())

#statics of the avergae of of women and men
#on who had a higher chance to survive
#women had more chance of surviving
# print(titanic_df[['Sex', 'Survived']].groupby('Sex').mean()) 

# print(titanic_df[['Sex','Pclass','Survived']].groupby(['Sex', 'Pclass']).mean()) 

#statitics on chance of having a sibling
# print(titanic_df[['SibSp', 'Survived']].groupby(['SibSp']).mean()) 

#parch is ratio to parent children
#the more children the less likely to survive
# print(titanic_df[['Parch', 'Survived']].groupby(['Parch']).mean()) 

#plotting

g = sns.FacetGrid(titanic_df, col='Survived')
g.map(plt.hist, 'Age')
# print(g)

# fig, ax = plt.subplots(1,3,figsize=(13,5))
# ax[0] = plt.hist()
# ax[1] = plt.bar()
# ax[2] = plt.scatter()
plt.show()