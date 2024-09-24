import numpy as np
a = np.array([[10, 20, 30],
              [40, 50, 60]])
b = np.array([2, 3, 4])
print(a+b)
print(a*b)

print(f"array{np.eye(4)*10}")

np_array4 = np.arange(0, 15)
np_array5 = np_array4.reshape((5, -1))
print(np_array5)

np_array6 = np.linspace(0, 10, 1000)
print(np_array6)    