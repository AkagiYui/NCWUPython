s = 'http://sports.sina.com.cn/'
print(s.count('t'))  # 输出 t 出现的次数
print(s.find('com'))  # com 出现的位置
print(s.replace('.', '_'))  # 用_替换.
print(s[7:13], s[-12:-8])  # 分别用正向反向切片提取sports和sina
print(s.upper())  # 字母全大写
print(len(s))  # 字符串长度
print(s + 'index')  # 字符串拼接