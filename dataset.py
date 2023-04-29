#importing pandas library

import pandas as pd
 
#loading data

titanic = pd.read_csv('...\input\train.csv')
# View first five rows of the dataset
titanic.head()
titanic.isnull().sum()
import seaborn as sns

import matplotlib.pyplot as plt
 
# Countplot

sns.catplot(x ="Sex", hue ="Survived", 

kind ="count", data = titanic)
# Group the dataset by Pclass and Survived and then unstack them

group = titanic.groupby(['Pclass', 'Survived'])

pclass_survived = group.size().unstack()
 
# Heatmap - Color encoded 2D representation of data.

sns.heatmap(pclass_survived, annot = True, fmt ="d")
# Violinplot Displays distribution of data 
# across all levels of a category.

sns.violinplot(x ="Sex", y ="Age", hue ="Survived", 

data = titanic, split = True)  

# Adding a column Family_Size

titanic['Family_Size'] = 0

titanic['Family_Size'] = titanic['Parch']+titanic['SibSp']
 
# Adding a column Alone

titanic['Alone'] = 0

titanic.loc[titanic.Family_Size == 0, 'Alone'] = 1
 
# Factorplot for Family_Size

sns.factorplot(x ='Family_Size', y ='Survived', data = titanic)
 
# Factorplot for Alone

sns.factorplot(x ='Alone', y ='Survived', data = titanic)
# Divide Fare into 4 bins

titanic['Fare_Range'] = pd.qcut(titanic['Fare'], 4)
 
# Barplot - Shows approximate values based 
# on the height of bars.

sns.barplot(x ='Fare_Range', y ='Survived', 

data = titanic)
# Countplot

sns.catplot(x ='Embarked', hue ='Survived', 

kind ='count', col ='Pclass', data = titanic)