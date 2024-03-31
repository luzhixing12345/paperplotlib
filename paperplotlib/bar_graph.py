from typing import List
from .graph import Graph


class BarGraph(Graph):
    def __init__(self) -> None:
        super().__init__()

        # 柱状图宽度 [0-1] (default 0.8)
        self.bar_width = 0.3
        # self.bar_width = 1

    def plot(self, x_data: List[float], y_data: List[float]):
        """
        填入数据
        """
        # x 轴坐标等距
        xticks = range(len(x_data))
        self.ax.bar(xticks, y_data, width=self.bar_width)
        
        # x 轴标签和位置的映射
        self.ax.set_xticks(xticks, x_data)
