import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
箱线图，面积图，六边形箱图，密度曲线图
'''


def test_views():
    plt.rcParams['font.sans-serif'] = ['Songti SC']
    plt.rcParams['axes.unicode_minus'] = False

    # df5 = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])

    # 箱线图
    # df5.plot.box(figsize=(8, 6))
    # plt.show()

    # color = {
    #     "boxes": "DarkGreen",
    #     "whiskers": "DarkOrange",
    #     "medians": "DarkBlue",
    #     "caps": "Gray",
    # }

    # 箱线图-颜色
    # df5.plot.box(color=color, sym="r+", figsize=(8, 6))
    # plt.show()

    # 箱线图-水平
    # df5.plot.box(vert=False, color=color, figsize=(8, 6))
    # plt.show()

    # df6 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])

    # 面积图
    # df6.plot.area(alpha=0.7, figsize=(8, 6))
    # plt.show()

    # df7 = pd.DataFrame(np.random.randn(1000, 2), columns=["a", "b"])
    # 六边形箱图
    # df7["b"] = df7["b"] + np.arange(1000)
    # df7.plot.hexbin(x="a", y="b", gridsize=25, figsize=(8, 6))
    # plt.show()

    # 密度曲线图
    # df8 = pd.Series(np.random.randn(1000))
    # df8.plot(kind='kde', figsize=(8, 6))
    # plt.show()


if __name__ == '__main__':
    test_views()
