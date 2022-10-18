# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input('请输入一行字符：')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        letters += 1
    elif c == ' ':
        space += 1
    elif c in '0123456789':
        digit += 1
    else:
        others += 1

print('英文字母个数：', letters)
print('空格个数：', space)
print('数字个数：', digit)
print('其他字符个数：', others)
