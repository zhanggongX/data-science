import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
更多样式，seaborn
'''


def test_views():
    plt.rcParams['font.sans-serif'] = ['Songti SC']
    plt.rcParams['axes.unicode_minus'] = False

    df6 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])

    # 如果对默认生成的图形不满意，可以通过 seaborn 来修改绘图主题或者修改绘图后端
    # 主题1
    # sns.set_palette("pastel", 8)
    # df6.plot.area(alpha=0.7, figsize=(8, 6))
    # plt.show()

    # 主题2
    # sns.set_palette("Blues_r", 8)
    # df6.plot.area(figsize=(8, 6))
    # plt.show()

    # 主题3
    # sns.set_palette("magma", 8)
    # df6.plot.area(figsize=(8, 6))
    # plt.show()

    # 修改后端
    # 修改pandas默认绘图引擎为plotly
    # pd.set_option("plotting.backend", "plotly")
    # df6.plot.area()
    # plt.show()


if __name__ == '__main__':
    test_views()
