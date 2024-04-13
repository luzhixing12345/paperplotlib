import matplotlib.pyplot as plt

# 假设我们有一些数据点
x = [1, 2, 3, 4, 5]  # x坐标
y = [2, 4, 6, 8, 10]  # y坐标

# 计算刻度间距,这里我们假设数据点的数量和范围允许我们设置相同的刻度间距
# 为了简化,我们选择一个简单的间距,例如2
tick_spacing = 2

# 计算x轴和y轴的刻度位置
x_ticks = range(min(x), max(x) + tick_spacing, tick_spacing)
y_ticks = range(min(y), max(y) + tick_spacing, tick_spacing)

# 创建一个新的图形
plt.figure()

# 绘制折线图
plt.plot(x, y, marker='o')  # 'o'表示数据点上会有圆圈标记

# 设置x轴和y轴的刻度
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# 添加标题和轴标签
plt.title('坐标轴刻度间距相同的折线图')
plt.xlabel('X轴')
plt.ylabel('Y轴')

# 显示网格(可选)
plt.grid(True)

# 显示图表
plt.show()