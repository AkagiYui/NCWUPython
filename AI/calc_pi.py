import random

n = 1_000_000  # 样本数量

cnt = 0
for i in range(1, n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if x ** 2 + y ** 2 <= 1:
        cnt += 1
print(4 * cnt / n)
