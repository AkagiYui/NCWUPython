"""
现有一个字典存放着学生的成绩
分别是 语文 数学 英语

1. 每门成绩均大于等于85的学生的学号
2. 每个学号对应的平均分和总分，保留2位小数
3. 按总分升序排列的学号列表
"""

d = {
    '01': [67, 88, 45],
    '02': [97, 68, 85],
    '03': [97, 98, 95],
    '04': [67, 48, 45],
    '05': [82, 58, 75],
    '06': [96, 49, 65],
}


def get_high_score_students():
    """每门成绩均大于等于85的学生的学号"""
    result = []
    for k, v in d.items():
        if min(v) >= 85:
            result.append(k)
    return result


def get_average_and_total_score():
    """每个学号对应的平均分和总分，保留2位小数"""
    result = {}
    for k, v in d.items():
        result[k] = (round(sum(v) / len(v), 2), sum(v))
    return result


def get_sorted_students():
    """按总分升序排列的学号列表"""
    t = get_average_and_total_score()
    return sorted(t, key=lambda x: t[x][1])


if __name__ == '__main__':
    print(get_high_score_students())
    print(get_average_and_total_score())
    print(get_sorted_students())
