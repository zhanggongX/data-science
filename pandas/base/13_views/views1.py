import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
折线图
'''


def test_views():
    plt.rcParams['font.sans-serif'] = ['Songti SC']
    plt.rcParams['axes.unicode_minus'] = False

    ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    ts = ts.cumsum()
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
    df = df.cumsum()

    # 绘制 df 第一列的折线图
    # df['A'].plot()
    # plt.show()

    # 将 df 的四列分别放在四个子图上
    # df.plot(subplots=True)
    # plt.show()

    # 绘制 df 全部列的折线图
    # df.plot()
    # plt.show()

    # 绘制 df 全部列的折线图，将大小调整为 1000*600 来让图片更美观
    # df.plot(figsize=(10, 6))
    # plt.show()

    # 添加标题
    # df.plot(figsize=(10, 6), title='hello pandas')
    # plt.show()

    # 添加表格
    # df.plot(figsize=(10, 6), title='hello pandas', grid=True)
    # plt.show()

    # 添加轴标签
    # df.plot(figsize=(10, 6), title='hello pandas', grid=True, xlabel='时间', ylabel='数量')
    # plt.show()

    # 调整刻度大小
    # df.plot(figsize=(10, 6), title='hello pandas', grid=True, xlabel='时间', ylabel='数量', fontsize=13)
    # plt.show()

    # 调整文字大小
    # df.plot(figsize=(10, 6), grid=True, fontsize=13)
    # plt.title("hello pandas", size=17)
    # plt.xlabel('时间', size=15)
    # plt.ylabel('数量', size=15)
    # plt.show()

    # 图例位置，将图例位置调整到左下角
    # df.plot(figsize=(10, 6), grid=True, fontsize=13)
    # plt.title("hello pandas", size=17)
    # plt.xlabel('时间', size=15)
    # plt.ylabel('数量', size=15)
    # plt.legend(loc=3)
    # plt.show()

    # 双y轴
    # A、B使用一个y轴，CD使用一个y轴
    # ax = df.plot(secondary_y=['A', 'B'], figsize=(10, 6), fontsize=13)
    # ax.set_ylabel('CD')
    # ax.right_ax.set_ylabel('AB')
    # ax.legend(loc=2)
    # plt.title("早起Python", size=17)
    # plt.xlabel('时间', size=15)
    # plt.ylabel('数量', size=15)
    # plt.legend(loc=1)
    # plt.show()


if __name__ == '__main__':
    test_views()
