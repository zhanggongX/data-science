import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
合并数据
'''


def test_merge_data():
    left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                         'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

    right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                          'B': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5']
                          })

    # 按单键连接
    # df = pd.merge(left, right, on='key')

    # 按多键连接
    # df = pd.merge(left, right, on=['key1', 'key2'])

    # 左外连接
    # pd.merge(left, right, how='left', on=['key1', 'key2'])

    # 右外连接
    # pd.merge(left, right, how='right', on=['key1', 'key2'])

    # 全外连接
    # pd.merge(left, right, how='outer', on=['key1', 'key2'])

    # 内连接
    # pd.merge(left, right, how='inner', on=['key1', 'key2'])

    # 重复索引，给名字重复的列添加后缀
    # pd.merge(left, right, on='k', suffixes=['_l', '_r'])


if __name__ == '__main__':
    test_merge_data()
