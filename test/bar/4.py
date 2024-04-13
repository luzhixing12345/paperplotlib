import sys

sys.path.append("..")
sys.path.append("../paperplotlib")

import paperplotlib as ppl

import numpy as np

# 设定数组的行数a和列数b
a = 6
b = 4
y = np.random.randint(10, 100, size=(a, b))

group_names = ["Canneal", "Memcached", "XSBench", "Graph500", "HashJoin", "BTree"]
column_names = [f"socket{i}" for i in range(b)]

graph = ppl.BarGraph()
graph.plot_2d(y, group_names, column_names)
# graph.x_label = "The number of data"
# graph.y_label = "Throughput (Mbps)"
# graph.width_picture = True
# graph.add_line(50)
graph.y_lim = (0, 100)
graph.save("test.png")
