import pandas as pd
import numpy as np

'''
统计
nunique 可以统计指定轴上不唯一的元素数量
'''


def test_explode():
    df = pd.DataFrame({'A': [4, 5, 6], 'B': [4, 1, 1]})
    print(df)

    # 按列统计
    # df = df.nunique()
    # print(df)

    # 按行统计
    # df = df.nunique(axis=1)
    # print(df)


if __name__ == '__main__':
    test_explode()
