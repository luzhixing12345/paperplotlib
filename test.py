import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import paperplotlib as ppl
import unittest
import numpy as np


class Test(unittest.TestCase):
    
    def test_bar_1d(self):
        x = [2, 4, 8, 16, 32]
        y = [2, 4, 8, 16, 32]
        graph = ppl.BarGraph()
        graph.plot(x, y)
        graph.x_label = "The number of data"
        graph.y_label = "Throughput (Mbps)"

        graph.save()

    
    def test_bar_2d(self):
        # 设定数组的行数a和列数b
        a = 8  # 例如:5行
        b = 4  # 例如:3列

        # 使用numpy的random.randint函数生成一个a行b列的随机整数数组
        # 假设我们想要的随机数范围是从0到99
        y = np.random.randint(10, 100, size=(a, b))

        group_names = [f"group {i}" for i in range(a)]
        column_names = [f"column {i}" for i in range(b)]

        g1 = ppl.BarGraph()
        g1.plot_2d(y, group_names, column_names)
        g1.x_label = "The number of data"
        g1.y_label = "Throughput (Mbps)"
        g1.width_picture = True
        g1.add_line(50)
        g1.save()
        
        g2 = ppl.BarGraph()
        g2.plot_2d(y, group_names, column_names, 0)
        
        g3 = ppl.BarGraph()
        a = 6
        b = 10
        y = np.random.randint(10, 100, size=(a, b))
        group_names = [f"group {i}" for i in range(a)]
        column_names = [f"column {i}" for i in range(b)]
        g3.plot_2d(y, group_names, column_names)
    
    def test_line_1d(self):
        x = [2, 4, 8, 16, 32]
        y = [2, 4, 8, 16, 32]
        graph = ppl.LineGraph()
        graph.plot(x, y)
        graph.x_label = "The number of data"
        graph.y_label = "Throughput (Mbps)"
        graph.y_lim = (0, 50)
        graph.disable_x_ticks = True
        graph.disable_points = True
        graph.save()
    
    def test_line_2d(self):
        a = 5
        b = 6
        y = np.random.randint(10, 100, size=(a, b))

        x_data = [i ** 2 for i in range(1, b+1)]
        line_names = [f"line {i}" for i in range(b)]

        g1 = ppl.LineGraph()
        g1.plot_2d(x_data, y, line_names)
        g1.x_label = "The number of data"
        g1.y_label = "Throughput (Mbps)"
        g1.save()



if __name__ == "__main__": # pragma: no cover
    unittest.main()