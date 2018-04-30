#Import libraries
import pandas as pd
import numpy as np

#load dataset
#press ctrl+i  for help
dataset=pd.read_csv('Data.csv')
#X=dataset.values[:,0:3]
#Y=dataset.values[:,-1]

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
print(X)
#checking shape of data
dim=dataset.shape
print("Dimensions of data",dim)

#data preprocessing

#Step 1 - Handling Missing Values
#Using Imputer technique
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy='mean',axis=0)
#X[:,1:3]=imputer.fit(X[:,1:3])
#X[:,1:3]=imputer.transform(X[:,1:3])

X[:,1:3]=imputer.fit_transform(X[:,1:3])
X



#Label Encoding
 from sklearn.preprocessing import LabelEncoder
 encode=LabelEncoder()
 X[:,0]=encode.fit_transform(X[:,0])
 print(X)
 
 #OneHotEncoding

from sklearn.preprocessing  import OneHotEncoder
hotencode=OneHotEncoder(categorical_features=[0])
X=hotencode.fit_transform(X).toarray()
print(X)



#Feature Scaling


