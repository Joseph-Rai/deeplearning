
import numpy as np

X = np.array([1,2])
print(X.shape) # 배열의 형상

W = np.array([[1,3,5],[2,4,6]])
print(W)
print(W.shape) # 배열의 형상

Y = np.dot(X,W) # 행렬 X와 W의 곱
print(Y) # 결과 출력