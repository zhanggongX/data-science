import pandas as pd
import numpy as np

'''
数据展开
'''


def test_explode():
    df = pd.DataFrame({'A': [[0, 1, 2], 'foo', [], [3, 4]],
                       'B': 1,
                       'C': [['a', 'b', 'c'], np.nan, [], ['d', 'e']]})

    print(df)

    # 单列展开
    # df = df.explode('A')
    # print(df)

    # pandas版本 >= 1.3 才可以完成
    df = df.explode(list('AC'))
    print(df)


if __name__ == '__main__':
    test_explode()
