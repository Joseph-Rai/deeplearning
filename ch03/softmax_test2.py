import numpy as np


a = np.array([1010, 1000, 900])
print(np.exp(a) / np.sum(np.exp(a))) # 제대로 계산되지 않는다

c = np.max(a) # c = 1010 (최대값)
print(a - c) 

print(np.exp(a - c) / np.sum(np.exp(a - c)))