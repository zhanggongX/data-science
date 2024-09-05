import pandas as pd
import numpy as np

'''
map 与 applymap
pandas 中的 map 和 applymap 可以对指定列（map）或整个数据框（applymap）工作
完成替换、格式化、计算等操作，是 Pandas 数据分析中十分重要的工具。
'''


def test_map():
    df1 = pd.DataFrame({'A': ['A0', 'A1', np.nan, 'A3'],
                        'B': ['B0', np.nan, 'B3', np.nan],
                        'C': ['C0', 'C1', 'C2', np.nan],
                        'D': np.random.randn(4),
                        'E': np.random.randn(4),
                        'F': np.random.randn(4)},
                       index=[0, 1, 2, 3])


    print(df1)

    # 基本使用, 将 df1 第一列中的 A0 替换为 cat，A3 替换为 rabbit，其余为设置为NaN（缺失值）
    # df1['A'] = df1['A'].map({'A0': 'cat', 'A3': 'rabbit'})
    # print(df1)

    # 将 df1 第 1 列中的字符末尾追加 hello
    # df1['A'] = df1['A'].map(lambda x: f'{x} hello')
    # print(df1)

    # 跳过缺失值
    # df1['B'] = df1['B'].map(lambda x: f'{x} hello', na_action='ignore')
    # print(df1)

    # 自定义函数
    # def mapfun(x):
    #     return str(x) + "hello"
    # df1['C'] = df1['C'].map(mapfun, na_action='ignore')
    # print(df1)

    # pplymap可以对整个 dataframe 工作，现在将 df1 的最后三列保留两位小数
    # df1[['D', 'E', 'F']] = df1[['D', 'E', 'F']].applymap(lambda x: "%.2f" % x)
    # print(df1)


if __name__ == '__main__':
    test_map()
