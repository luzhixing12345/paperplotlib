from typing import List, Tuple, Union
from .graph import Graph
from .color import COLOR
import numpy as np


class StackBarGraph(Graph):
    """
    堆叠条形图
    """

    def __init__(self, style_id: int = 1, subplots: Tuple[int, int] = None) -> None:
        super().__init__(style_id, subplots)

        self.percentage = False  # 是否转换为百分比
        # 方向
        self.direction = "vertical"  # or horizontal

        self._bar_width = 0.3
        self.thinkness = 0.5 # [0-1] 越大收缩越多

    def adjust_graph(self):
        
        left_margin = self.thinkness  # 可以根据需要调整空白的大小
        right_margin = self.thinkness
        
        if self.direction == "vertical":
            self.fig.set_size_inches(4, 6)
            current_xlim = self.ax.get_xlim()
            # 设置新的 x 轴范围
            self.ax.set_xlim([current_xlim[0] - left_margin, current_xlim[1] + right_margin])
        elif self.direction == "horizontal":
            self.fig.set_size_inches(16, 4)
            current_ylim = self.ax.get_ylim()
            # 设置新的 y 轴范围
            self.ax.set_ylim([current_ylim[0] - left_margin, current_ylim[1] + right_margin])
        else:
            raise ValueError("direction must be vertical or horizontal")

    def plot(self, data: List[float], labels: List[str], name: str = ""):
        """
        @param x_data: x 轴数据
        @param y_data: labels
        """

        colors = COLOR.get_colors(len(labels), self.style_id)
        cumulative = 0

        if self.percentage:
            data = np.array(data) / np.sum(data) * 100

        for data, color, label in zip(data, colors, labels):
            if self.direction == "vertical":
                self.ax.bar(
                    [name],
                    data,
                    color=color,
                    bottom=cumulative,
                    label=label,
                    width=self._bar_width,
                    edgecolor="black",
                    linewidth=0.5,
                )
            else:
                self.ax.barh(
                    [name],
                    data,
                    color=color,
                    left=cumulative,
                    label=label,
                    height=self._bar_width,
                    edgecolor="black",
                    linewidth=0.5,
                )

            cumulative += data

        self.set_label_legend(labels, position="w", alignment="|")
