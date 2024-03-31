import paperplotlib as ppl

x = [2, 4, 8, 16, 32]
y = [0.1, 0.5, 0.7, 0.9, 1.0]

graph = ppl.BarGraph()
graph.plot(x, y)
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"

graph.save("test.png")
