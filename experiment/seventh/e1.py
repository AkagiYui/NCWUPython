# 在windows下新建一个文本文件yzy.txt，文件内容如下
# 编写程序读取并输出该文件的内容，要求使用一次性读取整个文件内容和逐行读取文件内容两种方式

# 一次性读取整个文件内容
with open('yzy.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# 逐行读取文件内容
with open('yzy.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
