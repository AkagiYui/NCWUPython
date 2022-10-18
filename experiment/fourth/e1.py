li = []  # 定义一个空列表

# 访问
li.append(1)  # 在列表末尾添加一个元素
li.insert(0, 2)  # 在列表指定位置插入一个元素
li[1] = 3  # 修改列表指定位置的元素

# 列表扩充
li = li + [3, 4, 5]  # 在列表末尾拼接一个列表
li.extend([6, 7, 8])  # 在列表末尾拼接一个列表
li = li * 2  # 将列表重复两次

# 删除元素
del li[0]  # 删除列表指定位置的元素
li.pop(0)  # 删除列表指定位置的元素
li.remove(7)  # 删除列表中第一个值为7的元素

# 其他常用操作
print(len(li))  # 获取列表长度
print(3 in li)  # 判断列表中是否存在3
print(7 not in li)  # 判断列表中是否不存在7
print(li.index(3))  # 获取列表中第一个值为3的元素的索引
print(li.count(3))  # 获取列表中3的个数

# 列表遍历
for i in range(len(li)):
    print(li[i], end=' ')
print()
for i in li:
    print(i, end=' ')
print()

# 列表排序
print(sorted(li))  # 返回一个新的列表，该列表是原列表的排序副本
li.sort()  # 对列表进行排序

# 列表的复制
li2 = li.copy()  # 返回一个新的列表，该列表是原列表的复制副本
li3 = li  # 将li3指向li，li3和li指向同一个列表

# 删除
li.clear()  # 清空列表
del li  # 删除列表
