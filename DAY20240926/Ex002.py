from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

# X = [174, 152, 138, 128, 186]
# y = [71, 55, 46, 38, 88]
# plt.scatter(X, y, color='red')
#
# regression = linear_model.LinearRegression()   # Tensor 2 인 형태로
# X = [[174], [152], [138], [128], [186]]
# y = [71, 55, 46, 38, 88] # y 는 상관없음
#
# regression.fit(X, y)
# print(f"기울기는 : {regression.coef_}")
# print(f"바이어스 : {regression.intercept_}")
# y_hat = regression.predict(X)
# print(y_hat)
# my_weight = regression.predict([[175]])
# print(f"My weight : {my_weight}")
# plt.plot(X, y_hat, color='blue', linewidth=4)
# plt.show()

X = np.array([174, 152, 138, 128, 186])
y = np.array([71, 55, 46, 38, 88])

# 데이터 정규화 (Min-Max 정규화 사용)
X_min, X_max = np.min(X), np.max(X)
y_min, y_max = np.min(y), np.max(y)
X_norm = (X - X_min) / (X_max - X_min)
y_norm = (y - y_min) / (y_max - y_min)

W = 0  # 기울기
b = 0  # 절편
lrate = 0.01  # 학습률
epochs = 1000  # 반복 횟수
n = int(len(X_norm))  # 입력 데이터의 개수

# 경사 하강법
for i in range(epochs):
    y_pred_norm = W*X_norm + b  # 정규화된 예측값
    dW = (2/n) * sum(X_norm * (y_pred_norm-y_norm))
    db = (2/n) * sum(y_pred_norm-y_norm)
    W = W - lrate * dW  # 기울기 수정
    b = b - lrate * db  # 절편 수정

# 정규화된 파라미터를 원래 스케일로 변환
W_original = W * (y_max - y_min) / (X_max - X_min)
b_original = (b * (y_max - y_min) + y_min) - (W * X_min * (y_max - y_min) / (X_max - X_min))

# 기울기와 절편을 출력한다.
print(f"기울기(W): {W_original:.4f}, 절편(b): {b_original:.4f}")

# 예측값을 만든다.
y_pred = W_original*X + b_original

# 입력 데이터를 그래프 상에 찍는다.
plt.scatter(X, y)
# 예측값은 선그래프로 그린다.
plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red')
plt.show()

