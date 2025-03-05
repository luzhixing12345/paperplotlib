import matplotlib

# 非交互式 GUI 使用 Agg
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
from typing import List, Optional, Union, Tuple
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as fm


class Graph:
    """
    图表
    """
    def __init__(self, style_id: int = 1, subplots: Tuple[int, int] = None) -> None:
        self.style_id = style_id
        self.subplots = subplots

        if subplots is not None:
            self.fig, self.ax = plt.subplots(subplots[0], subplots[1])
        else:
            self.fig = plt.figure(figsize=(8, 4))
            self.ax = self.fig.add_subplot(111)

        # -- configuation --
        self.x_label: Optional[str] = None  # x轴标签
        self.y_label: Optional[str] = None  # y轴标签
        self.width_picture = False  # 是否是宽图
        self.grid = "y"  # 网格线 x | y | xy | None
        self.y_lim: Optional[Tuple[float, float]] = None

        # 基本属性
        self.grid_color = "#dedede"  # 网格线颜色
        self.grid_style = "-"  # 网格线类型 - | --
        self.grid_width = 1  # 网格线宽度
        self.grid_alpha = 0.8  # 网格线透明度

        # 保存图片
        self.dpi = 300
        self.bbox_inches = "tight"  # 适当上下左右留白

        self.title: Optional[str] = None  # 图表标题

        font_path = f"{os.path.dirname(__file__)}/font/consola-1.ttf"
        fm.fontManager.addfont(font_path)
        plt.rcParams["font.family"] = "Consolas"

        # legend
        self.legend_labels = None
        self.legend_loc = None
        self.legend_bbox_to_anchor = None
        self.legend_ncols = None
        self.legend_font_size = 'medium'

    def plot(self, x_data: List[float], y_data: List[float]):  # pragma: no cover
        """
        填入数据
        """
        raise NotImplementedError("请在子类中实现此方法")

    def plot_2d(
        self, y_data: List[List[float]], group_names: List[str], column_names: List[str], emphasize_index: int = -1
    ):  # pragma: no cover
        """
        绘制二维柱状图

        ## Parameters
        y_data: 二维列表,每个元素为一组数据
        group_names: 每个组的名称
        column_names: 每一列的名称
        """
        raise NotImplementedError("请在子类中实现此方法")

    def _create_graph(self):  # pragma: no cover
        self._check_config()

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

        if self.title is not None:
            self.fig.text(0.5, -0.02, self.title, ha="center", fontsize=14, weight="bold")

        if self.legend_labels is not None:
            self.legend = self.ax.legend(
                self.legend_labels,
                loc=self.legend_loc,  # 居中置顶
                ncols=self.legend_ncols,  # 横向排布
                bbox_to_anchor=self.legend_bbox_to_anchor,  # 置于图外侧
                handlelength=1,  # 图例长宽, 修改为正方形
                handleheight=1,  # 图例长宽, 修改为正方形
                handletextpad=0.4,  # 缩短文字和图例的间距
                fontsize=self.legend_font_size,  # 图例文字大小
            )

    def adjust_graph(self):
        """
        子类中可以重写该函数来调整图表
        """

    def save(self, path: str = "result.png"):
        """
        保存图片
        """
        self._create_graph()
        self.adjust_graph()
        plt.tight_layout()
        plt.savefig(path, dpi=self.dpi, bbox_inches=self.bbox_inches)
        print(f"save picture in {path}")

    def _check_config(self):
        """
        检查配置的属性是否设置的合理
        """
        assert self.grid in ["x", "y", "xy", None], "grid 参数值只能是 x | y | xy | None"
        assert self.width_picture in [True, False], "width_picture 参数值只能是 True | False"

    def set_label_legend(self, column_names, position: str = "w", alignment: str = "-"):
        """
        position should be 1 or 2 of 'wasd'

        w/a/s/d means up/left/down/right in keyboard
        """
        self.legend_labels = column_names

        # https://matplotlib.org/stable/api/legend_api.html#module-matplotlib.legend
        self.legend_loc = "upper center"
        self.legend_bbox_to_anchor = (0.5, 1.15)
        self.legend_ncols = len(column_names)

        # legend position

        # bbox_to_anchor
        # x:相对于图形的水平位置(通常 0 到 1 的值,1 表示图的最右边).
        # y:相对于图形的垂直位置(通常 0 到 1 的值,1 表示图的顶部)
        if position == "w":
            self.legend_loc = "upper center"
            self.legend_bbox_to_anchor = (0.5, 1.15)

        elif position == "d":
            self.legend_loc = "upper left"
            self.legend_bbox_to_anchor = (1.05, 1)

        elif position == "wd":
            self.legend_loc = "upper right"
            self.legend_bbox_to_anchor = None

        # legend alignment
        if alignment == "-":
            self.legend_ncols = len(column_names)
        elif alignment == "|":
            self.legend_ncols = 1
        elif type(alignment) == int:
            self.legend_ncols = alignment

    def adjust_legend(self, position: str = None, alignment: str = None, bbox_to_anchor: Tuple[float, float] = None, font_size: int = None):

        if position:
            self.legend_loc(position)

        if alignment:
            if alignment == "-":
                self.legend_ncols = len(self.legend_labels)
            elif alignment == "|":
                self.legend_ncols = 1
            elif type(alignment) == int:
                self.legend_ncols = alignment
            else:
                raise ValueError("alignment should be int or '-' or '|'")

        if bbox_to_anchor:
            self.legend_bbox_to_anchor = bbox_to_anchor

        if font_size:
            self.legend_font_size = font_size