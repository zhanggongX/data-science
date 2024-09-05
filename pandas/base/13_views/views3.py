import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
直方图
'''


def test_views():
    plt.rcParams['font.sans-serif'] = ['Songti SC']
    plt.rcParams['axes.unicode_minus'] = False

    df3 = pd.DataFrame(
        {
            "a": np.random.randn(1000) + 1,
            "b": np.random.randn(1000),
            "c": np.random.randn(1000) - 1,
        },
        columns=["a", "b", "c"], )

    # 默认直方图
    # df3.plot(kind='hist', figsize=(10, 6))
    # plt.show()

    # 修改透明度
    # df3.plot(kind='hist', figsize=(10, 6), alpha=0.5)
    # plt.show()

    # 修改小区间，设置小区间为20个
    # df3.plot(kind='hist', figsize=(10, 6), alpha=0.5, bins=20, stacked=True)
    # plt.show()

    # 将3个直方图拆分为3个子图
    # df3.diff().hist(alpha=0.5, bins=20, figsize=(10, 6))
    # plt.show()


if __name__ == '__main__':
    test_views()
