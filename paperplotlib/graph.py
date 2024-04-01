import matplotlib.pyplot as plt
from typing import List, Optional
from .color import COLOR


def check_dimensions(lst):
    dimensions = 0
    while isinstance(lst, list):
        dimensions += 1
        if len(lst) == 0:  # 如果子列表为空,则直接跳出循环
            break
        lst = lst[0]  # 递归检查子列表

    return dimensions


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
        self.grid = "y"  # x | y | xy | None
        self.grid_color = "#dedede"  # 网格线颜色
        self.grid_style = "-"  # 网格线类型 - | --
        self.grid_width = 1  # 网格线宽度
        self.grid_alpha = 0.8  # 网格线透明度

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
        self.check_config()
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)

        if self.grid is not None:
            if "x" in self.grid:
                self.ax.xaxis.grid(
                    True,
                    linestyle=self.grid_style,
                    linewidth=self.grid_width,
                    color=self.grid_color,
                    alpha=self.grid_alpha,
                )
            if "y" in self.grid:
                self.ax.yaxis.grid(
                    True,
                    linestyle=self.grid_style,
                    linewidth=self.grid_width,
                    color=self.grid_color,
                    alpha=self.grid_alpha,
                )
            self.ax.set_axisbelow(True)
        plt.savefig(path, dpi=self.dpi, bbox_inches=self.bbox_inches)

    def check_config(self):
        """
        检查配置的属性是否设置的合理
        """
        assert self.grid in ["x", "y", "xy", None], "grid 参数值只能是 x | y | xy | None"
