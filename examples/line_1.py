
# 将上级目录加入环境变量
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import paperplotlib as ppl
import numpy as np

# 100个数据
y = np.random.randint(10, 100, size=(100,))
x = range(100)

graph = ppl.LineGraph()
graph.plot(x,y)
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"
graph.disable_x_ticks = True
graph.disable_points = True
graph.save("line_1.png")