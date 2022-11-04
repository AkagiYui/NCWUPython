"""
绘制下列函数的图形：
    （1）f(x)=sin(x)+x^2, x∈[0,2π]
    （2）f(x)=x^3+2*x^2+1, x∈[-2,2]
"""

import math
import matplotlib.pyplot as plt

# f(x)=sin(x)+x^2, x∈[0,2π]
x = [i / 100 for i in range(0, 628)]  # 0, 0.01, 0.02, ..., 6.27
y = [math.sin(i) + i ** 2 for i in x]
plt.title('f(x)=sin(x)+x^2, x∈[0,2π]')  # 设置标题
plt.plot(x, y)
plt.show()

# f(x)=x^3+2*x^2+1, x∈[-2,2]
x = [i / 100 for i in range(-200, 201)]  # -2, -1.99, -1.98, ..., 2
y = [i ** 3 + 2 * i ** 2 + 1 for i in x]
plt.title('f(x)=x^3+2*x^2+1, x∈[-2,2]')  # 设置标题
plt.plot(x, y)
plt.show()
