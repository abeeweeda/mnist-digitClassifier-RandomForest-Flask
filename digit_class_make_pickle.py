import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import numpy as np

data = pd.read_csv(filepath)
'''
you can download the file from here or from anywhere its the mnist train.csv
https://drive.google.com/file/d/0B5DfT9EqluqzUlVfb0dOMTBUMVU/view

'''
#print(data.columns)
y_train = data.pop('label')
X_train = data
#print(X_train.columns)

# here we are using RandomForest Classifier for modelling , n_jobs=-1 for using all the cores of the CPU

#parameter grid for GridSerchCV
# param_grid = {
#     'n_estimators': [100, 150, 200, 300, 350],
#     'max_features': ['auto', 'sqrt', 'log2']
# }

estimator = RandomForestClassifier(n_jobs=-1, n_estimators=300, random_state=42)

#when using GridSearchCV use the below
#classifier = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=5)

#fitting the model 
estimator.fit(X_train, y_train)

# import pickle for saving the trained (fitted) model
import pickle
with open('digitClass.pickle', 'wb') as f:
   pickle.dump(estimator, f)