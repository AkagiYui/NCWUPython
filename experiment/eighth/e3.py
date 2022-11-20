"""
表1  每件产品的原料费、工资支付、管理费
产品	原料费	工资支付	管理费
A	0.6 1.8 0.6
B	1.8 2.4 1.2
C	0.9 1.5 0.9

表2  每个季度生产每种产品的数量
产品	第一季度	第二季度	第三季度	第四季度
A	4000	4500	4500	4000
B	2000	2600	2400    2200
C	5800    6200	6000	5000

请利用numpy库编程实现：
（1）输出该工厂四个季度生产A、B、C三种产品所需的成本总和。
（2）输出该工厂第一季度生产A、B、C三种产品所需的总成本。
（3）分别输出该工厂每个季度生产所有产品的原料费总成本、人工费总成本和管理费总成本，
并把这些数据以二维数组的形式写入文件cost_product.csv中，元素之间用英文逗号分隔。
（4）绘制子图1，在该子图中绘制折线，显示四个季度A、B、C三种产品的产量变化趋势，
横轴标签设置为“季度”，纵轴标签设置为“产量”。
（5）绘制子图2，在该子图中绘制饼图，显示第一季度生产A、B、C三种产品所花费的原料成本、人工成本和管理费成本的比值，
显示百分比（保留两位小数），饼图的标签对应显示“原料”、“人工”和“管理”。
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 创建数据
sheet_cost = np.array([
    [0.6, 1.8, 0.6],  # 产品A：原料费 工资支付 管理费
    [1.8, 2.4, 1.2],  # 产品B：原料费 工资支付 管理费
    [0.9, 1.5, 0.9],  # 产品C：原料费 工资支付 管理费
])
sheet_count = np.array([
    [4000, 4500, 4500, 4000],  # 产品A：第一季度 第二季度 第三季度 第四季度
    [2000, 2600, 2400, 2200],  # 产品B：第一季度 第二季度 第三季度 第四季度
    [5800, 6200, 6000, 5000],  # 产品C：第一季度 第二季度 第三季度 第四季度
])

# 输出该工厂四个季度生产A、B、C三种产品所需的成本总和。
# 成本总和 = 产品A费用*数量 + 产品B费用*数量 + 产品C费用*数量
cost_each_product = sheet_cost.sum(axis=1)  # 每个产品的费用，每行求和
count_each_product = sheet_count.sum(axis=1)  # 每个产品的数量
total_cost = cost_each_product.dot(count_each_product)  # 总费用，矩阵乘法
print(f'该工厂四个季度生产A、B、C三种产品所需的成本总和：{total_cost}万元')

# 输出该工厂第一季度生产A、B、C三种产品所需的总成本。
# 总成本 = 产品A第一季度数量*费用 + 产品B第一季度数量*费用 + 产品C第一季度数量*费用
count_quarter = sheet_count[:, 0]  # 第一季度的数量，每列取第一个元素
total_cost = count_quarter.dot(cost_each_product)
print(f'该工厂第一季度生产A、B、C三种产品所需的总成本：{total_cost}万元')

# 分别输出该工厂每个季度生产所有产品的原料费总成本、人工费总成本、管理费总成本。
# 第1季度：原料费总成本 人工费总成本 管理费总成本
# 第2季度：原料费总成本 人工费总成本 管理费总成本
# 第3季度：原料费总成本 人工费总成本 管理费总成本
# 第4季度：原料费总成本 人工费总成本 管理费总成本
data_table = sheet_cost.T.dot(sheet_count).T  # T: 转置
for i, d in enumerate(data_table):
    print(f"第{i + 1}季度 原料费总成本{d[0]}万元 人工费总成本{d[1]}万元 管理费总成本{d[2]}万元")

# 把这些数据以二维数组的形式写入文件cost_product.csv中，元素之间用英文逗号分隔
with open('cost_product.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data_table)

# 绘图
mpl.rc('font', family='SimHei', size=16)  # 设置字体，解决中文乱码问题
plt.figure(figsize=(8, 12))  # 设置画布大小
plt.subplots_adjust(hspace=0.5)  # 设置子图间距
plt.suptitle('AkagiYui的matplotlib的绘图实验')  # 设置总标题

# 绘制子图1，在该子图中绘制折线，显示四个季度A、B、C三种产品的产量变化趋势，
# 横轴标签设置为“季度”，纵轴标签设置为“产量”。
plt.subplot(2, 1, 1)  # 占用2行1列，第1个子图
plt.title('四个季度A、B、C三种产品的产量变化趋势')  # 设置标题
plt.xlabel('季度')  # 设置横轴标签
plt.ylabel('产量（件）')  # 设置纵轴标签
plt.xticks(range(4), ['1', '2', '3', '4'])  # 设置横轴刻度
for i, d in enumerate(sheet_count):
    plt.plot(d, ['-.', '-', ':'][i], label=f'产品{i + 1}')  # 绘制折线图
    for ii, dd in enumerate(d):
        plt.text(ii, dd, dd, ha='center', va='bottom')  # 绘制折线图上的数据
plt.legend()  # 显示图例

# 绘制子图2，显示第一季度生产A、B、C三种产品所花费的原料成本、人工成本和管理费成本的比值，显示百分比（保留两位小数），
# 饼图的标签对应显示“原料”、“人工”和“管理”。
plt.subplot(2, 1, 2)  # 占用2行1列，第2个子图
plt.title('第一季度生产三种产品所花费的\n原料成本、人工成本和管理费成本占比')
plt.pie(data_table[0], labels=['原料', '人工', '管理'], autopct='%.2f%%')  # 绘制饼图
plt.show()
