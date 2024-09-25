import numpy as np

# np_value1 = np.array([[1, 1], [2, 2], [3, 3]], dtype=np.int32)
# np_value2 = np.insert(np_value1, 1, 4, axis=0) # 원본 수정이 안됨
# np_value3 = np.insert(np_value1, 1, 4, axis=1)
# print(np_value2)
# print(np_value3)

# np_value = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]])
# print(np_value)
# print(np_value[0, 1])
#
# np_value1 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
# print(f"평균값 : {np_value1.mean()}")

np_value = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np_value1 = np_value.reshape(2, -1)
print(np_value1)

np_value2 = np.random.randn(10) * 10 + 175
print(np_value2)
print(np_value2.round(2))
print(np_value2.astype(int))

np.random.seed(2024)
np_value10 = np.random.normal(165, 10, (10, 10))
print(np_value10)

a = np.array([[1, 2], [1, -3]])
b = np.array([6,1])
s = np.linalg.solve(a, b)
print(s)