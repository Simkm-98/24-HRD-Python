import numpy as np
from sklearn import datasets

(diabetes_X, diabetes_y) = datasets.load_diabetes(return_X_y=True)
print(diabetes_X)
print(diabetes_X.shape)
print(diabetes_y)
print(diabetes_y.shape)
bmi = diabetes_X[:,2]
print(bmi)
print(bmi.shape)

diabetes_X_new = diabetes_X[:,np.newaxis, 2]
print(diabetes_X_new)
print(diabetes_X_new.shape)

from sklearn.model_selection import train_test_split

(X_train, X_test, y_train, y_test) = train_test_split(diabetes_X_new, diabetes_y,
                                                      train_size=0.8, random_state=0)
# print(X_train[10])
from sklearn import linear_model
regression = linear_model.LinearRegression() # class
regression.fit(X_train, y_train)

y_predict = regression.predict(X_test)
print(y_predict)
print(y_test)

import matplotlib.pyplot as plt

plt.scatter(y_test, y_predict)
plt.show()