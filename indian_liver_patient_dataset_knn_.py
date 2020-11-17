# -*- coding: utf-8 -*-
"""Indian Liver Patient Dataset knn .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iH7UN8GSAcXkMiexODhTw6tyKfaD3LpR

# **import library**
"""

import pickle
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
np.random.seed(42)

"""# **load data**"""

#load data
load_data=pd.read_csv(r"/content/Indian Liver Patient Dataset (ILPD).csv")

"""#view sample data"""

print(load_data.head())

"""# **handel missing data**"""

print(load_data.info())

load_data.dropna(how="any",inplace=True)

print(load_data.info())

"""# ** map labled data **"""

load_data["gender"] =load_data["gender"].map({"Female": 0 , "Male":1 })
X=load_data.drop('is_patient',axis=1)
y=load_data['is_patient']

"""#**split data to train \ test**"""

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

"""#**choose model**"""

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)

"""#**train model**"""

model.fit(x_train,y_train)

"""# **validate modle**"""

print(model.score(x_train , y_train))
print(model.score(x_test , y_test))

"""#**save model**"""

pickle.dump(model , open(r"mushrooms.pkl","wb"))