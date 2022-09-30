for k in range(1, 11):
    w = input()
    if 'AEIOUaeiou'.find(w[0]) >= 0:
        print(w)

# explain in Chinese
# 1. 循环10次
# 2. 输入一个单词
# 3. 判断单词的第一个字母是否是元音字母
# 4. 如果是，输出这个单词
# 5. 如果不是，继续循环
