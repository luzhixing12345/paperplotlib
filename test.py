import paperplotlib as ppl
import numpy as np

# 随机生成一个 5 x 7 的数据
a = 4
b = 5
y = np.random.randint(10, 100, size=(a, b))

# 初始化一个对象
graph = ppl.LineGraph(3)

# 传入数据/组/列的文字信息

li = [f"column {i}" for i in range(b)]
graph.plot_2d()

# 调整x/y轴文字
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"
graph.add_line(50)

# 保存图片
graph.save()