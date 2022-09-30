table = [
    ['王平', '男', 1, 1, 0, 0],
    ['李丽', '女', 0, 1, 0, 1],
    ['陈小梅', '女', 0, 0, 1, 0],
    ['孙洪涛', '男', 0, 1, 1, 1],
    ['方亮', '男', 1, 0, 1, 0],
]

# 报名大于等于2项的人数
n_2 = 0
for i in table:
    if i.count(1) >= 2:
        n_2 += 1
print(f'报名大于等于2项的人数：{n_2}')

# 女生的报名情况
for i in table:
    if i[1] == '女':
        print(f'{i[0]}的报名情况：{i[2:]}')

# 报名3000m的学生姓名和性别
for i in table:
    if i[3] == 1:
        print(f'{i[0]}的性别：{i[1]}')
