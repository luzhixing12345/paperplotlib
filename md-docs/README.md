# paperplotlib

paperplotlib 是基于 matplotlib 的论文实验数据绘图库, 意在快速绘制论文实验结果部分中常见的柱状图/折线图

本库提供了一组 **论文实验数据图的默认样式**, 以及一组相对简洁的 API 调用

一些绘制的示例代码和结果图见: [paperplotlib 示例](https://luzhixing12345.github.io/paperplotlib/articles/md-docs/使用示例/)

## 安装

```bash
pip install paperplotlib
```

## 快速开始

```python
import paperplotlib as ppl
import numpy as np

# 随机生成一个 5 x 7 的数据
a = 5
b = 7
y = np.random.randint(10, 100, size=(a, b))

group_names = [f"group {i}" for i in range(a)]
column_names = [f"column {i}" for i in range(b)]

graph = ppl.BarGraph()
graph.plot_2d(y, group_names, column_names)
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"
graph.save()
```

![](https://raw.githubusercontent.com/luzhixing12345/paperplotlib/master/images/paperplotlib/result.png)

使用文档: [paperplotlib document](https://luzhixing12345.github.io/paperplotlib/)

## 参考

- [matplotlib](https://matplotlib.org/stable/users/index.html)
- [matplotlib.pyplot的使用总结大全](https://www.zhihu.com/tardis/zm/art/139052035?source_id=1003)