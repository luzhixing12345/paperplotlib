# 将上级目录加入环境变量
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import paperplotlib as ppl
import numpy as np

a = 3
b = 50
x = [i for i in range(b)]
y = np.random.randint(10, 100, size=(a, b))


line_names = ["line 1", "line 2", "line 3", "line 4", "line 5"]

graph = ppl.LineGraph()
graph.plot_2d(x, y, line_names)

graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"
# graph.disable_x_ticks = True
# graph.disable_points = True
graph.title = "Line 2"
graph.save("line_2.png")
