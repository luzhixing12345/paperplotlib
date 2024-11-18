import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import paperplotlib as ppl
import unittest
import numpy as np


import paperplotlib as ppl

# 创建一个堆叠条形图
stackbar_graph = ppl.StackBarGraph()

# 设置数据
labels = [
    "alloc_migration_target",
    "try_to_migrate",
    "move_to_new_folio",
    "folio_add_lru" "remove_migration_ptes",
    "migrate_folio_done",
]

# move_to_new_folio(30.311% 545/1798)
# try_to_migrate(19.188% 345/1798)
# migrate_folio_done(8.732% 157/1798)
# alloc_migration_target(8.676% 156/1798)
# remove_migration_ptes(8.287% 149/1798)
# folio_add_lru(6.897% 124/1798)

# 百分比数据(按图片中的顺序)
percentages = [8.676, 19.188, 30.311, 6.897, 8.287, 8.732]

# 绘制堆叠条形图
stackbar_graph.direction = "horizontal"
stackbar_graph.thinkness = 0.2
stackbar_graph.plot(percentages, labels, name="migrate_page_batch")
stackbar_graph.adjust_legend(alignment=3, font_size=20)
# 保存图像
stackbar_graph.save("stackbar_graph.png")
