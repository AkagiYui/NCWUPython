"""
2.	编写程序新建一个文本文件yzy2.txt，并写入下面两行内容：
游子吟
唐代：孟郊
接着读取题目1中文件yzy.txt的内容，追加到文件yzy2.txt末尾，最后文件yzy2.txt的内容应该如下：
"""

with open('yzy2.txt', 'w', encoding='utf-8') as f:
    f.writelines(['游子吟', '唐代：孟郊', '\n'])

with open('yzy.txt', 'r', encoding='utf-8') as f:
    with open('yzy2.txt', 'a', encoding='utf-8') as f2:
        f2.write(f.read())
