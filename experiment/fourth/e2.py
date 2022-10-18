# 从键盘输入10个整数，放入列表中，输出该列表的元素个数，最大值，最小值，元素和，平均值。

li = []
for _ in range(10):
    li.append(int(input()))
print(len(li))
print(max(li))
print(min(li))
print(sum(li))
print(sum(li) / len(li))
