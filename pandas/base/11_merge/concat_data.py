import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
合并数据
'''


def test_concat_data():
    left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                         'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

    right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                          'B': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5']
                          })

    # 默认拼接-垂直拼接-df1、df2、df3
    # pd.concat([df1, df2, df3])

    # 重置索引，垂直拼接df1和df4，并按顺序重新生成索引
    # pd.concat([df1, df4], ignore_index=True)

    # 横向拼接 df1、df4
    # pd.concat([df1, df4], axis=1)

    # 横向拼接，只取结果的交集
    # pd.concat([df1, df4], axis=1, join='inner')

    # 横向拼接，取指定。只取包含 df1 索引的部分
    # pd.concat([df1, df4], axis=1).reindex(df1.index)

    # 拼接 df1、df2、df3，同时新增一个索引（x、y、z）来区分不同的表数据来源
    # pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])


if __name__ == '__main__':
    test_concat_data()
