import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


dachshund_length = [77, 78, 85, 83, 73, 77, 73, 80]
dachshund_height = [25, 28, 29, 30, 21, 22, 17, 35]
samoyed_length = [75, 77, 86, 86, 79, 83, 83, 88]
samoyed_height = [56, 57, 50, 53, 60, 53, 49, 61]

plt.scatter(dachshund_length, dachshund_height, c='red', marker=".", label="Dachshund")
plt.scatter(samoyed_length, samoyed_height, c='blue', marker="*", label="Samoyed")
# plt.show()

d_data = np.column_stack((dachshund_length, dachshund_height))
s_data = np.column_stack((samoyed_length, samoyed_height))
d_label = np.zeros(len(d_data))
s_label = np.ones((len(s_data)))
# print(d_data)
# print(d_label)
# print(s_data)
# print(s_label)

dogs = np.concatenate((d_data, s_data))
labels = np.concatenate((d_label, s_label))
print(dogs)
print(labels)

dog_classes = {0:'Dachshund', 1:'Samoyed'}

new_dog = [[79, 35]]

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(dogs, labels)
new_dog_predict = knn.predict(new_dog)
print(f"Data : {new_dog}, 결과 : {dog_classes[new_dog_predict[0]]}")


plt.scatter(new_dog[0][0], new_dog[0][1], c='green', marker='p')
plt.show()

# 400마리 숙제