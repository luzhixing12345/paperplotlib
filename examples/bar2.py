import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import paperplotlib as ppl

x = [2, 4, 8, 16, 32]
y = [2, 4, 8, 16, 32]
graph = ppl.BarGraph()
graph.plot(x, y)
graph.save('bar2.png')