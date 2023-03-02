# 栅栏密码 解密

secret = 'TEESCPEHRIAIHR'
ms = (2, 3, 4)  # 栅栏数

for m in ms:  # 尝试不同的栅栏数
    n = len(secret) // m  # 每个栅栏的字符数

    # 分组
    groups = []
    for i in range(m):
        groups.append(secret[i * n:(i + 1) * n])

    # 解密
    plain = ''
    for i in range(n):
        for j in range(m):
            plain += groups[j][i]

    print(n, groups, plain)
