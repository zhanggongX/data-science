import pandas as pd
import numpy as np

'''
删除数据
'''


def test_delete_data():
    path = '../../../data/东京奥运会奖牌数据.csv'
    df = pd.read_csv(path)

    # 修改列名
    df.rename(columns={'Unnamed: 2': '金牌数',
                       'Unnamed: 3': '银牌数',
                       'Unnamed: 4': '铜牌数'}, inplace=True)
    df.set_index("排名", inplace=True)

    # 删除 df 第一行
    df = df.drop(1)

    # 删除条件行
    df = df.drop(df[df.金牌数 < 20].index)

    # 删除列
    df.drop(columns=['国家奥委会代码'], inplace=True)

    # 删除 df 的 1\2 列
    print(df)
    df.drop(df.columns[[1, 2]], axis=1, inplace=True)

    print(df)


if __name__ == '__main__':
    test_delete_data()
