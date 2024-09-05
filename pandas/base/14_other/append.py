import pandas as pd
import numpy as np

'''
数据添加
'''


def test_append():
    df = pd.DataFrame(
        {
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"],
            "C": ["C0", "C1", "C2", "C3"],
            "D": ["D0", "D1", "D2", "D3"],
        },
        index=[0, 1, 2, 3],
    )

    s1 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])
    s2 = pd.DataFrame({"A": ['s1'], "B": ['s2'], "C": ['s3'], "D": ['s4']})
    dicts = [{"A": 1, "B": 2, "C": 3, "X": 4}, {"A": 5, "B": 6, "C": 7, "Y": 8}]

    # 末尾追加
    # result = df.append(s1, ignore_index=True)
    # print(result)

    # 指定位置追加
    # df1 = df.iloc[:2, :]
    # df2 = df.iloc[2:, :]
    # df3 = pd.concat([df1, s2, df2])
    # print(df3)

    # 添加字典
    # result = df.append(dicts, ignore_index=True, sort=False)
    # print(result)


if __name__ == '__main__':
    test_append()
