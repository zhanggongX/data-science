import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
透视表
'''


def test_pivot_table():
    path = '../../../data/某超市销售数据.csv'
    df = pd.read_csv(path)

    # 制作各省「平均销售额」的数据透视表
    # df = pd.pivot_table(df, values=['销售额'], index='省/自治区')

    # 制作各省「销售总额」的数据透视表
    # df = pd.pivot_table(df, values=['销售额'], index='省/自治区', aggfunc='sum')

    # 制作各省「销售总额」与「平均销售额」的数据透视表
    # df = pd.pivot_table(df, values=['销售额'], index='省/自治区', aggfunc=['mean', 'sum'])

    # 制作各省市「销售总额」与「利润总额」的数据透视表
    # df = pd.pivot_table(df, values=['销售额', '利润', '数量'], index='类别', aggfunc='sum')

    # 制作「各省市」与「不同类别」产品「销售总额」的数据透视表
    # df = pd.pivot_table(df, values=['销售额'], index=['省/自治区', '类别'], aggfunc='sum')

    # 制作各省市「不同类别」产品的「销售总额」透视表
    # df = pd.pivot_table(df, values=['销售额'], index=['省/自治区'], columns='类别', aggfunc='sum')

    # 制作「各省市」、「不同类别」产品「销售量与销售额」的「均值与总和」的数据透视表，并在最后追加一行『合计』
    # df = pd.pivot_table(df, values=['销售额', '数量'], index=['省/自治区', '类别'], aggfunc=['mean', 'sum'], margins=True)

    # 制作「各省市」、「不同类别」产品「销售量与销售额」的「均值与总和」的数据透视表，并在最后追加一行『合计』
    # 查询 「类别」 等于 「办公用品」 的详情
    # df = pd.pivot_table(df, values=['销售额', '数量'], index=['省/自治区', '类别'], aggfunc=['mean', 'sum'],margins=True)
    # df = df.query('类别 == ["办公用品"]')

    # 逆透视就是将宽的表转换为长的表，透视表进行逆透视，其中不需要转换的列为『数量』列
    # df = pd.pivot_table(df, values=['销售额', '利润', '数量'], index='类别', aggfunc='sum')
    # df = df.melt(id_vars=['数量'], var_name='分类', value_name='金额')

    print(df)


if __name__ == '__main__':
    test_pivot_table()
