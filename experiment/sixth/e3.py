# 编写一个函数，接收一个列表参数，函数返回该列表中所有正数之和。在主程序中调用测试该函数。

def sum_positive_number(numbers):
    s = 0
    for n in numbers:
        if n > 0:
            s += n
    return s


li = [1, 2, 3, -1, -2, -3]
print(sum_positive_number(li))
