import matplotlib.pyplot as plt
from typing import List, Optional, Union, Tuple


class Graph:
    """
    图表
    """

    def __init__(self) -> None:
        self.fig = plt.figure(figsize=(8, 4))
        self.ax = self.fig.add_subplot(111)
        
        # -- configable --
        self.x_label: Optional[str] = None # x轴标签
        self.y_label: Optional[str] = None # y轴标签
        self.width_picture = False # 是否是宽图
        self.grid = "y"  # 网格线 x | y | xy | None
        self.y_lim: Optional[Tuple[float, float]] = None
        self.emphasize_index: Optional[int] = None # 柱状图中高亮某一列
        # -- configable --

        # 基本属性
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

    def save(self, path: str = "result.png"):
        """
        保存图片
        """
        self.check_config()
        if self.width_picture:
            self.fig.set_size_inches(16, 4)
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
        
        if self.y_lim is not None:
            self.ax.set_ylim(self.y_lim)
        
        plt.savefig(path, dpi=self.dpi, bbox_inches=self.bbox_inches)

    def check_config(self):
        """
        检查配置的属性是否设置的合理
        """
        assert self.grid in ["x", "y", "xy", None], "grid 参数值只能是 x | y | xy | None"
        assert self.width_picture in [True, False], "width_picture 参数值只能是 True | False"