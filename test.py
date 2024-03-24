import matplotlib.pyplot as plt

# 数据:X轴的类别标签和Y轴的数值
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 20, 15, 30]

# 创建一个新的图表
plt.figure()

# 绘制柱状图
plt.bar(categories, values)

# 添加标题和轴标签
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# 显示图表
plt.show()