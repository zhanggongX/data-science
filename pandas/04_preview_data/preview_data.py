import pandas as pd

'''
预览数据
'''


def test_preview_data():
    douban_top_250_path = '../../data/TOP250.txt'
    df = pd.read_table(douban_top_250_path, encoding='gb18030')

    # 看看数据多少行，多少列
    # print(df.shape)

    # 数据抽样 也就是随机查看一个样本
    # print(df.sample())

    # 看看数据前三行
    # print(df.head(3))

    # 看看数据结构，有无缺失
    # print(df.info())

    # 查看 数值型 列的统计信息，计数、均值什么的
    # print(df.describe())
    # round 2 保留两位小数, T 行转列。
    # print(df.describe().round(2).T)

    # 查看 离散型 列的统计信息，计数、频率什么
    print(df.describe(include=['O']))


if __name__ == '__main__':
    test_preview_data()
