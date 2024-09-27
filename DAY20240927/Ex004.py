from sklearn.preprocessing import MinMaxScaler
import numpy as np

X = np.array([174, 152, 138, 128, 186])
y = np.array([71, 55, 46, 38, 88])
X_new = X[:, np.newaxis] # tensor 1 증가
y_new = y[:, np.newaxis]
print(X_new)
print(y_new)

scaler = MinMaxScaler()
X = scaler.fit_transform(X_new)
y = scaler.fit_transform(y_new)
print(X)
print(y)

X = X.flatten()  # tensor 1 평탄화
y = y.flatten()
print(X)
print(y)

W = 1.0 # 기울기
b = 1.0

lr = 0.01
epochs = 1_000
n = len(X)
for _ in range(epochs):
    y_hat = W * X + b
    error = y_hat - y
    dW = (2 / n) * sum(X * error)
    db = (2 / n) * sum(error)
    W = W - lr * dW
    b = b - lr * db

print(f"W : {W}, b : {b}")

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_new, y)
print(f"W : {regression.coef_}, b : {regression.intercept_}")