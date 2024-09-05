import pandas as pd
import numpy as np

'''
compare 用于比较两个数据框之间的差异
'''


def test_compare():
    df = pd.DataFrame(
        {
            "col1": ["a", "a", "b", "b", "a"],
            "col2": [1.0, 2.0, 3.0, np.nan, 5.0],
            "col3": [1.0, 2.0, 3.0, 4.0, 5.0]
        },
        columns=["col1", "col2", "col3"],
    )

    df1 = df.copy()
    df1.loc[0, 'col1'] = 'c'
    df1.loc[2, 'col3'] = 4.0
    print(df1)

    # 默认比较
    # print(df.compare(df1))

    # 保留原数据框
    # print(df.compare(df1, keep_shape=True))

    # 保留原始相同的值
    # print(df.compare(df1, keep_shape=True, keep_equal=True))


if __name__ == '__main__':
    test_compare()
