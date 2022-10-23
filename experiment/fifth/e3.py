# 使用集合变量set_highjump和set_longjump分别存储参加跳高和跳远比赛的学生姓名。
# 统计两项比赛都参加的学生名单并输出
# 统计参加比赛的所有学生名单并输出
# 统计只参加跳高比赛的学生名单并输出
# 统计只参加跳远比赛的学生名单并输出
# 统计只参加一项比赛的学生名单并输出

set_highjump = {'李朋', '王宇', '张锁', '刘松山', '白旭', '李晓亮'}
set_longjump = {'王宇', '刘松山', '白旭', '唐英', '刘小雨', '宁成'}

set_all = set_highjump | set_longjump  # 使用|运算符求并集
print('参加比赛的所有学生名单：', set_all)

set_both = set_highjump & set_longjump  # 使用&运算符求交集
print('两项比赛都参加的学生名单：', set_both)

set_highjump_only = set_highjump - set_longjump  # 使用-运算符求差集
print('只参加跳高比赛的学生名单：', set_highjump_only)

set_longjump_only = set_longjump - set_highjump  # 使用-运算符求差集
print('只参加跳远比赛的学生名单：', set_longjump_only)

set_one = set_highjump ^ set_longjump  # 使用^运算符求对称差集（并集-交集）
print('只参加一项比赛的学生名单：', set_one)
