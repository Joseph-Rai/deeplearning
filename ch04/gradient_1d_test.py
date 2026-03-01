
from matplotlib import pyplot as plt
import numpy as np

from numerical_diff import numerical_diff
from gradient_1d import function_1


x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
# plt.show()

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))