import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import paperplotlib as ppl
import numpy as np

# 随机生成一个 5 x 7 的数据
a = 5
b = 7
y = np.random.randint(10, 100, size=(a, b))

# 初始化一个对象
graph = ppl.BarGraph()

# 传入数据/组/列的文字信息
group_names = [f"group {i}" for i in range(a)]
column_names = [f"column {i}" for i in range(b)]
graph.plot_2d(y, group_names, column_names)

# 调整x/y轴文字
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"

# 保存图片
graph.save("bar1.png")