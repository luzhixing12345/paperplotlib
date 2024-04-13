import matplotlib.pyplot as plt
import numpy as np

# 示例数据:类别、组1的值、组2的值
categories = ['Category A', 'Category B', 'Category C', 'Category D']
group1_values = [10, 20, 15, 30]
group2_values = [12, 25, 18, 33]

# 设置柱子的宽度
bar_width = 0.2

# 设置x轴的位置
r1 = np.arange(len(categories))
r2 = [x + bar_width for x in r1]

# 绘制组1的柱状图
plt.bar(r1, group1_values, width=bar_width, label='Group 1')

# 绘制组2的柱状图,并列于组1
plt.bar(r2, group2_values, width=bar_width, label='Group 2', color='orange')

# 添加标题和标签
plt.title('Multiple Side-by-Side Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# 设置横轴标签
plt.xticks([r + bar_width / 2 for r in r1], categories)

# 添加图例
plt.legend()

# 显示图表
plt.show()