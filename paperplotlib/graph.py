import matplotlib.pyplot as plt
from typing import List, Optional, Union
from .color import PLOT_COLOR


class Graph:
    """
    图表
    """

    def __init__(self) -> None:
        self.fig = plt.figure(figsize=(8, 4))
        self.ax = self.fig.add_subplot(111)
        self.x_label: Optional[str] = None
        self.y_label: Optional[str] = None

        # 基本属性

        # 保存图片
        self.dpi = 300
        self.bbox_inches = "tight"  # 适当上下左右留白

    def plot(self, x_data: List[float], y_data: List[float]):
        """
        填入数据
        """
        raise NotImplementedError("请在子类中实现此方法")

    def save(self, path: str = "result.png", wide_picture=False):
        """
        保存图片
        """
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        plt.savefig(path, dpi=self.dpi, bbox_inches=self.bbox_inches)
