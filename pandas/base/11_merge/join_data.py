import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
合并数据
'''


def test_join_data():
    left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                         'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5'],
                         'B': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5']})
    left.set_index('key', inplace=True)
    right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                          'C': ['C0', 'C1', 'C2', 'C3', 'C4', 'C5'],
                          'D': ['D0', 'D1', 'D2', 'C3', 'D4', 'D5']})
    right.set_index('key', inplace=True)

    # 组合 left 和 right，并按照 left 的索引进行对齐
    # df = left.join(right)

    # 取并集
    df = left.join(right, how='outer')

    # 取交集
    df = left.join(right, how='inner')

    # 按索引组合
    df = left.join(right, on='key')

    # 多索引组合
    # df = left.join(right, on=['key1', 'key2'])
    print(df)


if __name__ == '__main__':
    test_join_data()
