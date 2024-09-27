from sklearn.datasets import load_iris

iris = load_iris()
print(iris)

data = iris['data']
target = iris['target']
print(data)
print(data.shape)
print(target)
print(target.shape)

import pandas as pd
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(iris_df.head())

from sklearn.model_selection import train_test_split
(X_train, X_test, y_train, y_test) = train_test_split(data, target, train_size=0.8)

from  sklearn.neighbors import KNeighborsClassifier
k = 5

knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

y_predict = knn.predict(X_test)
print(y_predict)
print(y_test)

from sklearn import metrics
scores = metrics.accuracy_score(y_test, y_predict)
print(f"정확도 : {scores}")

new_flower = [[3.0, 4.0, 5.0, 2.0]]
new_flower_predict = knn.predict(new_flower)
print(new_flower_predict)