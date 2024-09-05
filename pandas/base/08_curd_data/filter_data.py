import pandas as pd
import numpy as np

'''
过滤数据
'''


def test_filter_data():
    path = '../../../data/东京奥运会奖牌数据.csv'
    df = pd.read_csv(path)

    # 修改列名
    df.rename(columns={'Unnamed: 2': '金牌数',
                       'Unnamed: 3': '银牌数',
                       'Unnamed: 4': '铜牌数'}, inplace=True)
    df.set_index("排名", inplace=True)

    # 提取 金牌数、银牌数、铜牌数 三列
    # df = df.iloc[:, [0, 1, 2, 3]]
    # df = df[['金牌数', '银牌数', '铜牌数']]

    # 筛选全部 奇数列
    # df = df.iloc[:, [i % 2 == 1 for i in range(len(df.columns))]]

    # 提取全部列名中包含 数 的列
    # df = df.loc[:, df.columns.str.endswith('数')]

    # 提取倒数后三列的10-20行
    # df = df.loc[10:20, '总分':]

    # 提取第 10 行
    # df = df.loc[9:9]

    # 提取第 10 行之后的全部行
    # df = df.loc[9:]

    # 提取 0-50 行，间隔为 3
    # df = df[:50:3]

    # 提取 金牌数 大于 30 的行
    # df = df[df['金牌数'] > 30]

    # 提取 金牌数 等于 10 的行
    # df = df.loc[df['金牌数'] == 10]

    # 提取 金牌数 不等于 10 的行
    # df = df.loc[~(df['金牌数'] == 10)]

    # 提取全部 奇数行
    # df = df[[i % 2 == 1 for i in range(len(df.index))]]

    # 提取 中国、美国、英国、日本、巴西五行数据
    # df = df.loc[df['国家奥委会'].isin(['中国', '美国', '英国', '日本', '巴西'])]
    # df = df.loc[(df['金牌数'] < 30) & (df['国家奥委会'].isin(['中国', '美国', '英国', '日本', '巴西']))]

    # 提取 国家奥委会 列中，所有包含 国的行
    # df = df[df.国家奥委会.str.contains('国')]

    # 提取 第 0 行第 2 列
    # df = df.iloc[0:1, [1]]
    # 提取 第 0-2 行第 0-2 列
    # df = df.iloc[0:2, [0, 1]]

    # 提取第 4 行，第 4 列的值
    # df = df.iloc[3, 3]

    # 提取行索引为 4 ，列名为 金牌数 的值
    # df = df.at[4, '金牌数']

    # 提取 国家奥委会 为 中国 的金牌数
    # df = df.loc[df['国家奥委会'] == '中国']
    # # 2 是索引值
    # df = df.loc[2]
    # df = df.at['金牌数']

    # 使用 query 提取 金牌数 + 银牌数 大于 15 的国家
    # df = df.query('金牌数+银牌数 > 15')

    # 使用 query 提取 金牌数 大于 金牌均值的国家
    # gold_mean = df['金牌数'].mean()
    # df.query(f'金牌数 > {gold_mean}')

    # isin - 筛选
    # df = df[df.国家奥委会.isin(['中国', '美国', '英国', '日本', '巴西'])]
    # df = df[~df.国家奥委会.isin(['中国', '美国', '英国', '日本', '巴西'])]

    # select_dtypes 可以筛选制定数据类型的列
    # df = df.select_dtypes(include=['int64'])

    # 数据类型为和浮点数的列
    # df = df.select_dtypes(include=['int', 'float64'])

    # 逆筛选
    # df = df.select_dtypes(exclude=['int', 'float64'])
    print(df)


if __name__ == '__main__':
    test_filter_data()
