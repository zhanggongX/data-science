import pandas as pd
import numpy as np

'''
修改数据
'''


def test_modify_data():
    path = '../../data/东京奥运会奖牌数据.csv'
    df = pd.read_csv(path)

    # 修改列名
    df.rename(columns={'Unnamed: 2': '金牌数',
                       'Unnamed: 3': '银牌数',
                       'Unnamed: 4': '铜牌数'}, inplace=True)

    # 将第一列（排名）设置为索引
    df.set_index("排名", inplace=True)

    # 修改索引名为 金牌排名
    df.rename_axis("金牌排名", inplace=True)

    # 将 ROC（第一列第五行）修改为 俄奥委会
    df.iloc[4, 0] = '俄奥委会'

    # 将金牌数列的数字 0 替换为 无
    # df['金牌数'] = df['金牌数'].replace(0, '无')

    # 将 无 替换为 缺失值
    # 将 0 替换为 None
    # df.replace(['无', 0], [np.nan, 'None'], inplace=True)

    # 将 金牌数 列类型修改为 int
    # df['金牌数'] = df['金牌数'].fillna('0').astype(int)

    # 新增一列 比赛地点，值为 东京
    # df['比赛地点'] = '东京'

    # df = df.replace('None', 0)
    # df['金银牌总数'] = df['金牌数'] + df['银牌数']

    # 新增一列 最多奖牌数量 列，值为该过金银牌数量种最多的一个奖牌数量
    # df['最多奖牌数量'] = df.bfill()[["金牌数", "银牌数", '铜牌数']].max(axis=1)

    # 如果一个国家的金牌数大于 30 则值为 是，反之为 否
    # df['金牌大于30'] = np.where(df['金牌数'] > 30, '是', '否')

    # 新增两列，分别是
    # 金铜牌总数（金牌数+铜牌数）
    # 银铜牌总数（银牌数+铜牌数）
    # df = df.assign(金铜牌总数=df.金牌数 + df.铜牌数, 银铜牌总数=df.银牌数 + df.铜牌数)

    # 新增一列金牌占比，为各国金牌数除以总金牌数
    # gold_sum = df['金牌数'].sum()
    # df.eval(f'金牌占比 = 金牌数 / {gold_sum}', inplace=True)

    # 在 df 末尾追加一行，内容为 0,1,2,3… 一直到 df 的列长度
    # df1 = pd.DataFrame([[i for i in range(len(df.columns))]], columns=df.columns)
    # df = pd.concat([df, df1], ignore_index=True)

    # 在第 2 行新增一行数据，即美国和中国之间
    # df1 = df.iloc[:1, :]
    # df2 = df.iloc[1:, :]
    # df3 = pd.DataFrame([[i for i in range(len(df.columns))]], columns=df.columns)
    # df = pd.concat([df1, df3, df2], ignore_index=True)

    print(df)


if __name__ == '__main__':
    test_modify_data()
