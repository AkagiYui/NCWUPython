# 接着读取题目1中文件yzy.txt的内容，追加到文件yzy2.txt末尾

with open('yzy.txt', 'r', encoding='utf-8') as f:
    with open('yzy2.txt', 'a', encoding='utf-8') as f2:
        f2.write(f.read())
