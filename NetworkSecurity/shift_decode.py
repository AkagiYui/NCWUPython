# 移位加密 解密

secret = 'mjqqt cnftrnsl xzwuwnx'

# 从1开始移位
m = 1
while m < 26:
    plain = ''
    for c in secret:
        if c == ' ':
            plain += ' '
        else:
            plain += chr(ord('a') + (ord(c) - ord('a') - m) % 26)
    print(m, plain)
    m += 1
