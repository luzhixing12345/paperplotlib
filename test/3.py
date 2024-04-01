import sys

sys.path.append("..")
sys.path.append("../paperplotlib")

import paperplotlib as ppl

import numpy as np

# 设定数组的行数a和列数b
a = 8  # 例如:5行
b = 4  # 例如:3列

# 使用numpy的random.randint函数生成一个a行b列的随机整数数组
# 假设我们想要的随机数范围是从0到99
y = np.random.randint(10, 100, size=(a, b))

group_names = [f"group {i}" for i in range(a)]
column_names = [f"column {i}" for i in range(b)]

graph = ppl.BarGraph()
graph.plot_2d(y, group_names, column_names)
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"
graph.width_picture = True
# graph.add_line(50)
graph.save("test.png")
