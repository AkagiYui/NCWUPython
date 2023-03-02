# 置换密码法：列换位法 加密

value = 'WHAT YOU CAN LEARN FROM THIS BOOK'
m = 5

# 删除空格
value = value.replace(' ', '')

# 加密
secret = ''
for i in range(m):
    secret += value[i::m]

print(secret)
