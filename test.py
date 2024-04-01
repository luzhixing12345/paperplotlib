import paperplotlib as ppl
import numpy as np

# 随机生成一个 5 x 7 的数据
a = 5
b = 8
y = np.random.randint(10, 100, size=(a, b))

group_names = [f"group {i}" for i in range(a)]
column_names = [f"column {i}" for i in range(b)]

graph = ppl.BarGraph()
graph.plot_2d(y, group_names, column_names)
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"
graph.save()
