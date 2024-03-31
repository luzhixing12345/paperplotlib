import re
import os
from typing import List, Dict


class Color:

    def __init__(self) -> None:
        self.colors: Dict[str, List[List[str]]] = {}
        self.name_map = {1: "one", 2: "two", 3: "three"}

    def add(self, name: str, hex_groups: List[List[str]]):
        self.colors[name] = hex_groups


def parse_colors() -> Color:
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

PLOT_COLOR = parse_colors()
