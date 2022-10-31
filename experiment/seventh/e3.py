# score.csv保存了10名考生3门课程的成绩，内容如下：考号,高级语言程序设计,高等数学,数据库原理
# 编写程序读取该文件内容，统计每门课程的平均分、最高分和最低分。

import csv
with open('score.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = [row for row in reader]
    for i in range(1, 4):
        scores = [int(row[i]) for row in data]
        print(f'第{i}门课程的平均分为{sum(scores) / len(scores)}')
        print(f'第{i}门课程的最高分为{max(scores)}')
        print(f'第{i}门课程的最低分为{min(scores)}')
