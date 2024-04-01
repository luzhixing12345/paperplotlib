import sys

sys.path.append("..")
sys.path.append("../paperplotlib")

import paperplotlib as ppl

x = [2, 4, 8, 16, 32]
y = [2, 4, 8, 16, 32]
graph = ppl.BarGraph()
graph.plot(x, y)
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"

graph.save("test.png")
