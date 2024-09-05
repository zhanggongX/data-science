import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
散点图
'''


def test_views():
    plt.rcParams['font.sans-serif'] = ['Songti SC']
    plt.rcParams['axes.unicode_minus'] = False

    df4 = pd.DataFrame(np.random.rand(50, 4), columns=["a", "b", "c", "d"])
    df4["species"] = pd.Categorical(["setosa"] * 20 + ["versicolor"] * 20 + ["virginica"] * 10)

    # 默认方法，制作散点图，X轴为 a，Y轴为 b
    # df4.plot.scatter(x="a", y="b", figsize=(8, 6))
    # plt.show()

    # 让散点的大小随着值变化
    # df4.plot.scatter(x="a", y="b", figsize=(8, 6), s=df4["c"] * 200)
    # plt.show()

    # 散点固定，调低透明度，增加黑色边缘线
    # df4.plot.scatter(x="a", y="b", figsize=(8, 6), marker='o', s=100, linewidths=1, alpha=0.8, edgecolors='black')
    # plt.show()

    # 将散点的颜色设置为渐变色
    # df4.plot.scatter(x="a", y="b", c="c", figsize=(8, 6), marker='o', s=100, linewidths=1, alpha=0.8,
    #                  edgecolors='black')
    # plt.show()

    # 分组绘制，将 ab 分为一组，cd分为一组，制作三散点图
    # ax = df4.plot.scatter(x="a", y="b", color="DarkBlue", label="Group 1", figsize=(8, 6), marker='o',
    #                       s=80, linewidths=1, alpha=0.8, edgecolors='black')
    # df4.plot.scatter(x="c", y="d", color="DarkGreen", label="Group 2", ax=ax, figsize=(8, 6), marker='o',
    #                  s=80, linewidths=1, alpha=0.8, edgecolors='black');
    # plt.show()


if __name__ == '__main__':
    test_views()
