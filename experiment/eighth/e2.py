"""
绘制下列函数的图形：
    （1）f(x)=sin(x)+x^2, x∈[0,2π]
    （2）f(x)=x^3+2*x^2+1, x∈[-2,2]
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# f(x)=sin(x)+x^2, x∈[0,2π]
x = np.arange(0, 2 * math.pi, 0.01)  # 0, 0.01, 0.02, ..., 6.27
y = np.sin(x) + x ** 2  # 这是用numpy进行数组运算
plt.title('f(x)=sin(x)+x^2, x∈[0,2π]')  # 设置标题
plt.plot(x, y)
plt.show()

# f(x)=x^3+2*x^2+1, x∈[-2,2]
x = np.arange(-2, 2, 0.01)  # -2, -1.99, -1.98, ..., 2
y = x ** 3 + 2 * x ** 2 + 1
plt.title('f(x)=x^3+2*x^2+1, x∈[-2,2]')  # 设置标题
plt.plot(x, y)
plt.show()
