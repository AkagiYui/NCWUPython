# 移位加密 解密

secret = 'mjqqt cnftrnsl xzwuwnx'

for i in range(1, 26):  # 从1开始移位
    plain = ''
    for c in secret:  # 遍历密文
        if c == ' ':  # 保留空格
            plain += ' '
        else:
            c = ord(c) - ord('a')  # 转换为相对于a的偏移量
            c = (c - i) % 26  # 移位
            c = c + ord('a')  # 转换为绝对偏移量
            plain += chr(c)  # 转换为字符
    print(i, plain)
