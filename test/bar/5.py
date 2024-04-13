import sys

sys.path.append("..")
sys.path.append("../paperplotlib")

import paperplotlib as ppl

import numpy as np

# 设定数组的行数a和列数b
a = 5
b = 5
y = np.random.rand(a, b)

group_names = ["A", "B", "C", "D", "F"]
column_names = ["DDR5:CXL-A = 100:0", "75:25", "50:50", "25:75", "0:100"]

graph = ppl.BarGraph()
graph.plot_2d(y, group_names, column_names, emphasize_index=0)
graph.x_label = "Workload"
graph.y_label = "Max QPS\nNormalized DDR 100%"
# graph.width_picture = True
# graph.add_line(50)
graph.y_lim = (0, 1.2)
graph.save("test.png")
