# 输出100～200间的全部素数，每行输出10个数。

c = 0
for i in range(100, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')
        c += 1
        if c % 10 == 0:
            print()
