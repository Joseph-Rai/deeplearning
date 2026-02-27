
import numpy as np

from softmax import softmax

a = np.array([0.3, 2.9, 4.0])

exp_a = np.exp(a) # 지수함수
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)


y2 = softmax(a)
print(y2)
print(np.sum(y2))