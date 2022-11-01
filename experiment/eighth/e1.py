"""
利用numpy库，创建两个ndarray数组A和B，两个数组的shape均为4X5，数组A的元素为
[[ 0, 1, 2, 3, 4],
 [ 5, 6, 7, 8, 9],
 [10, 11, 12, 13, 14],
 [15, 16, 17, 18, 19]]，
数组B的元素为：[[100, 101, 102, 103, 104],
             [105, 106, 107, 108, 109],
             [110, 111, 112, 113, 114],
             [115, 116, 117, 118, 119]]。
编写程序实现以下功能：
（1）	输出A+B、B-A、A*B、A/B、A2+B3的结果。
（2）	对A的中间两行和B的中间两行的元素进行求和，并输出。
（3）	输出A的数组轴个数rank、数组形状shape、数组大小和数组中每个元素占用的字节数。
"""

import numpy as np
array_a = np.arange(20).reshape(4, 5)
array_b = np.arange(100, 120).reshape(4, 5)

print(array_a + array_b, '\n')
print(array_b - array_a, '\n')
print(array_a * array_b, '\n')
print(array_a / array_b, '\n')
print(array_a ** 2 + array_b ** 3, '\n')

print(array_a[1:3, :].sum() + array_b[1:3, :].sum(), '\n')

print(array_a.ndim, array_a.shape, array_a.size, array_a.itemsize)
