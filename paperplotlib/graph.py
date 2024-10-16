import matplotlib
# 非交互式 GUI 使用 Agg
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from typing import List, Optional, Union, Tuple
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as fm

class Graph:
    """
    图表
    """

    def __init__(self, style_id: int = 1) -> None:
        self.style_id = style_id
        self.fig = plt.figure(figsize=(8, 4))
        self.ax = self.fig.add_subplot(111)
        
        # -- configuation --
        self.x_label: Optional[str] = None # x轴标签
        self.y_label: Optional[str] = None # y轴标签
        self.width_picture = False # 是否是宽图
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
        
        self.title: Optional[str] = None # 图表标题
        
        font_path = f'{os.path.dirname(__file__)}/consola-1.ttf'
        fm.fontManager.addfont(font_path)
        plt.rcParams['font.family'] = 'Consolas'
        # self.font_family = "Consolas" # 字体
        # 如果是 linux 
        # if os.name == 'posix':
        #     self.font_family = consolas_font.get_name()
        # self.colors: Optional[List[str]] = None

    def plot(self, x_data: List[float], y_data: List[float]): # pragma: no cover
        """
        填入数据
        """
        raise NotImplementedError("请在子类中实现此方法")

    def plot_2d(self, y_data: List[List[float]], group_names: List[str], column_names: List[str], emphasize_index: int = -1): # pragma: no cover
        """
        绘制二维柱状图

        ## Parameters
        y_data: 二维列表,每个元素为一组数据
        group_names: 每个组的名称
        column_names: 每一列的名称
        """
        raise NotImplementedError("请在子类中实现此方法")

    def _create_graph(self): # pragma: no cover
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
            self.fig.text(0.5, -0.02, self.title, ha='center', fontsize=14, weight='bold')

    def _adjust_graph(self):
        '''
        子类中可以重写该函数来调整图表
        '''

    def save(self, path: str = "result.png"):
        """
        保存图片
        """
        self._create_graph()
        self._adjust_graph()
        plt.savefig(path, dpi=self.dpi, bbox_inches=self.bbox_inches)
        print(f"保存成功:{path}")

    def _check_config(self):
        """
        检查配置的属性是否设置的合理
        """
        assert self.grid in ["x", "y", "xy", None], "grid 参数值只能是 x | y | xy | None"
        assert self.width_picture in [True, False], "width_picture 参数值只能是 True | False"