from .graph import Graph
from typing import List
from .color import COLOR
import matplotlib.ticker as ticker


class LineGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.grid = "xy"
        # https://matplotlib.org/stable/api/markers_api.html
        self.all_markers = [
            "o",
            "^",
            "x",
            "s",
            "D",
            "*",
            "+",
            "v",
            "p",
            "P",
            "h",
            "H",
            "1",
            "2",
            "3",
            "4",
            "X"
        ]
        self.disable_x_ticks = False # 是否禁用 x 轴刻度
        self.disable_points = False # 是否禁用点
        self.line_width = 1.5

    def _adjust_graph(self):
        
        # 线条宽度
        for line in self.ax.get_lines():
            line.set_linewidth(self.line_width)
        
        if self.disable_x_ticks:
            self.ax.xaxis.set_major_locator(ticker.NullLocator())
        if self.disable_points:
            # 修改 marker
            for line in self.ax.get_lines():
                line.set_marker('')
            # 修改图例中的 marker
            legend = self.ax.get_legend()
            if legend is not None:  # 检查图例是否存在
                for legend_line in legend.get_lines():
                    legend_line.set_marker('')

    def plot(self, x_data: List[int], y_data: List[float]):
        """
        绘制一维折线图

        ## Parameters
        x_data: x 轴数据
        y_data: y 轴数据
        """
        # x 轴坐标等距
        if x_data is None:
            x_data = range(len(y_data))
        x_ticks = range(len(x_data))
        self.ax.plot(x_ticks, y_data, linewidth=2, marker="o", markersize=5, color=COLOR.get_colors(1, self.style_id)[0])
        # x 轴标签和位置的映射
        self.ax.set_xticks(x_ticks, x_data)

    def plot_2d(self, x_data: List[int], y_data: List[List[float]], line_names: List[str], emphasize_index: int = -1):
        # x 轴坐标等距
        if x_data is None:
            x_data = range(len(y_data[0]))
        x_ticks = range(len(x_data))
        line_number = len(line_names)
        
        assert line_number <= len(self.all_markers), "markers 数量不足"    
        markers = self.all_markers[:line_number]
        colors = COLOR.get_colors(line_number, self.style_id, emphasize_index)
        for i, y in enumerate(y_data):
            self.ax.plot(x_ticks, y, linewidth=2, label=line_names[i], marker=markers[i], markersize=5, color=colors[i])
        # x 轴标签和位置的映射
        self.ax.set_xticks(x_ticks, x_data)
        self.legend = self.ax.legend(
            line_names,
            loc="upper center",  # 居中置顶
            ncols=line_number,  # 横向排布
            bbox_to_anchor=(0.5, 1.15),  # 置于图外侧
            handlelength=1,  # 图例长宽, 修改为正方形
            handleheight=1,  # 图例长宽, 修改为正方形
            handletextpad=0.4,  # 缩短文字和图例的间距
            fontsize="x-small" if line_number >= 7 else "medium",  # 图例文字大小
        )
