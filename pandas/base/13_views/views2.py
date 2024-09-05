import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
条形图
'''


def test_views():
    plt.rcParams['font.sans-serif'] = ['Songti SC']
    plt.rcParams['axes.unicode_minus'] = False

    df2 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])

    # 使用垂直条形图
    # df2.iloc[2].plot(kind='bar', figsize=(10, 6))
    # plt.show()

    # 使用水平条形图
    # df2.iloc[2].plot(kind='barh', figsize=(10, 6))
    # plt.show()

    # 多行-将df2的全部行在同一个画布上制作条形图
    # df2.plot(kind='bar', figsize=(10, 6))
    # plt.show()

    # 对条形图进行堆叠
    # df2.plot(kind='bar', figsize=(10, 6), stacked=True)
    # plt.show()

if __name__ == '__main__':
    test_views()
