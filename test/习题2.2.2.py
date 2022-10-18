# 计算外圆半径为16.2，内圆半径为9.4的圆环面积
# 保留小数点后两位

import math
r1 = 16.2
r2 = 9.4
print(f'圆环面积为：{math.pi * (r1 ** 2 - r2 ** 2):.2f}')
print('{:.2f}'.format(math.pi * (r1 ** 2 - r2 ** 2)))