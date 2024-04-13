import re
import os
import numpy as np
import matplotlib.colors as mcolors
from typing import List, Dict


class Color:

    def __init__(self) -> None:
        self.colors: Dict[str, Dict[int, List[str]]] = {}

    def add(self, name: str, hex_groups: List[List[str]]):
        self.colors[name] = {}
        for hex_group in hex_groups:
            self.colors[name][len(hex_group)] = hex_group

    def get_colors(self, color_num: int, style_id: int = 1, emphasize_index: int = -1) -> List[str]:
        if emphasize_index != -1:
            return self.get_emphasize(emphasize_index, color_num)
        # 对于更多颜色的情况, 采用渐变
        style_name = f"style-{style_id}"
        assert style_name in self.colors, f"{style_name} 不存在, 有效的样式为 {list(self.colors.keys())}"
            
        colors = self.colors[style_name].get(color_num)
        # 如果没有该数量的颜色, 采用渐变
        if colors is None:
            colors = generate_color_gradient(self.colors["cold"][2][0], self.colors["cold"][2][1], color_num)
        return colors

    def get_emphasize(self, index, color_num: int) -> List[str]:
        emphasized_color = "#ffc000"
        colors = generate_color_gradient(self.colors["cold"][2][0], self.colors["cold"][2][1], color_num)
        colors.insert(index, emphasized_color)
        return colors


def parse_colors() -> Color:
    """
    从 color.css 中解析颜色
    """
    with open(os.path.join(os.path.dirname(__file__), "color.css")) as f:
        content = f.read()

    plot_color = Color()
    css_classes = re.finditer(r"\.(.*?) \{(.*?)\}", content, re.DOTALL)
    for css_class in css_classes:
        color_name = css_class.group(1).strip()
        color_values = css_class.group(2).split("\n")
        hex_groups: List[List[str]] = []
        for color_value in color_values:
            if len(color_value) == 0:
                continue
            hex_values = re.findall(r"#[0-9a-fA-F]{6}", color_value)
            hex_groups.append(hex_values)
        plot_color.add(color_name, hex_groups)

    return plot_color


def hex_to_rgb(hex_color):
    # 将十六进制颜色代码转换为RGB元组
    return mcolors.hex2color(hex_color)


def rgb_to_hex(rgb_color):
    # 将RGB元组转换为十六进制颜色代码
    return mcolors.rgb2hex(rgb_color)


def generate_color_gradient(hex_color1, hex_color2, num_colors):
    # 将十六进制颜色代码转换为RGB元组
    color1 = hex_to_rgb(hex_color1)
    color2 = hex_to_rgb(hex_color2)

    # 生成颜色渐变
    r = np.linspace(color1[0], color2[0], num_colors)
    g = np.linspace(color1[1], color2[1], num_colors)
    b = np.linspace(color1[2], color2[2], num_colors)

    gradient_colors = [rgb_to_hex((r[i], g[i], b[i])) for i in range(num_colors)]
    return gradient_colors


COLOR = parse_colors()
