import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우의 경우
plt.rcParams['axes.unicode_minus'] = False

# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]
#
# plt.xlabel('X 축')
# plt.ylabel('Y 축')
# plt.plot(x, y)
# plt.show()
#
# x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# # y = [i**2 for i in x ] # list 형태
# x = np.array(x)
# y = x ** 2
# plt.xlabel('X 축')
# plt.ylabel('Y 축')
# plt.plot(x, y)
# plt.show()

# x = np.arange(-20, 20)
# y1 = 2 * x
# y2 = (1/3) * x ** 2 + 5
# y3 = -x ** 2 - 5
# plt.figure(figsize=(10, 6))
# plt.plot(x, y1, 'g-')
# plt.plot(x, y2, 'ro-')
# plt.plot(x, y3, 'b.-')
# plt.axis([-20, 20, -30, 30])
# plt.show()

x = np.linspace(0, 2 * np.pi, 1_000)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
plt.plot(x, y1, 'b', x, y2, 'r', x, y3, 'c')
plt.axis([0, 2 * np.pi, -2, 2])
plt.savefig("Sin-Cos-Tan.png")
plt.show()