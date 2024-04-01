import re
import os
from typing import List, Dict


class Color:

    def __init__(self) -> None:
        self.colors: Dict[str, List[List[str]]] = {}
        self.key_map = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
        }

    def add(self, name: str, hex_groups: List[List[str]]):
        self.colors[name[1:]] = hex_groups

    def get(self, key: int, emphasize: int = None):
        return self.colors[self.key_map[key]][0]
            


def parse_colors() -> Color:
    """
    从 color.css 中解析颜色
    """
    with open(os.path.join(os.path.dirname(__file__), "color.css")) as f:
        content = f.read()

    plot_color = Color()
    css_classes = re.finditer(r"(.*?) \{(.*?)\}", content, re.DOTALL)
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


COLOR = parse_colors()
