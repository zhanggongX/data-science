import pandas as pd
import numpy as np

'''
累加
'''


def test_cumsum():
    df = pd.DataFrame(np.arange(1, 37).reshape([9, 4]), columns=["A", "B", "C", "D"])
    df['item'] = ['Apple', 'Xiaomi', 'Huawei'] * 3

    print(df)

    # 按列累加
    # df = df[list('ABCD')].cumsum()
    # print(df)

    # 按行累加
    # df = df[list('ABCD')].cumsum(axis=1)
    # print(df)

    # 按照 item 按不同组对第 A 列进行累加
    # df = df.sort_values(['item']).reset_index(drop=True)
    # df['cusum'] = df.groupby('item')['A'].cumsum(axis=0)
    # print(df)


if __name__ == '__main__':
    test_cumsum()
