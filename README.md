# paperplotlib

paperplotlib 是基于 matplotlib 的论文实验数据绘图库, 意在快速绘制论文实验结果部分中常见的柱状图/折线图

本库提供了一组 **论文实验数据图的默认样式**, 以及一组相对简洁的 API 调用

一些绘制的示例代码和结果图见: [paperplotlib 示例]()

## 安装与使用

```bash
pip install paperplotlib
```

```python
import paperplotlib as ppl

x = [2, 4, 8, 16, 32]
y = [0.1, 0.5, 0.7, 0.9, 1.0]

graph = ppl.BarGraph()
graph.plot(x, y)
graph.x_label = "The number of data"
graph.y_label = "Throughput (Mbps)"

graph.save("test.png")
```

![](./test.png)

使用文档: [paperplotlib document](https://luzhixing12345.github.io/paperplotlib/)

## 参考

- [matplotlib](https://matplotlib.org/stable/users/index.html)
- [matplotlib.pyplot的使用总结大全](https://www.zhihu.com/tardis/zm/art/139052035?source_id=1003)
- [matplotlib.pyplot常用函数讲解大全(一)](https://zhuanlan.zhihu.com/p/139475633)
- [matplotlib.pyplot常用函数讲解大全(二)](https://zhuanlan.zhihu.com/p/139946399)