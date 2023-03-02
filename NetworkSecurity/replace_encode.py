# 置换密码法：列换位法 加密

plain = 'WHAT YOU CAN LEARN FROM THIS BOOK'  # 明文
m = 5  # 列数
c = 'X'  # 填充字符

# 加密
plain = plain.replace(' ', '')  # 删除空格
plain += c * (m - len(plain) % m)  # 填充不足的列
secret = ''
for i in range(m):
    secret += plain[i::m]

print(secret)
