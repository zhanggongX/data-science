import pandas as pd
import matplotlib.pyplot as plt
import datetime

'''
股票数据分析
'''


def stock_analysis():
    path1 = '../../data/stock/000001_daily.csv'
    path2 = '../../data/stock/000001_5min.csv'
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)

    # 将 df1 和 df2 的 日期 列转换为 pandas 支持的时间格式
    df1['日期'] = pd.to_datetime(df1['日期'])
    df2['时间'] = pd.to_datetime(df2['时间'])

    # 筛选出 df2 时间在 2021-08-03 09:35:00 与 2021-08-04 15:00:00 之间的数据
    # df = df2[(df2['时间'] > '2021-08-03 09:35:00') & (df2['时间'] < '2021-08-04 15:00:00')]

    # 筛选 df2 时间为 2021-08-03 的全部数据
    # df = df2.set_index('时间').truncate(after=pd.Timestamp('2021-08-04'))

    # df1 新增一列 涨跌，计算前后两日收盘价之差
    # df1['涨跌'] = df1.收盘.diff()

    # df1 新增一列 涨跌变化率，计算前后两日收盘价之差的变化率
    # df1['涨跌变化率'] = (df1.收盘.pct_change()).apply(lambda x: format(x, '.2%'))

    # 计算收盘价的5日移动均线
    # df = df1.收盘.rolling(window=5).mean()

    # 计算并绘制收盘价的5日移动均线
    # df = df1.收盘.rolling(window=5).mean().plot()

    # 同时计算并绘制 df1 的收盘价、5日均线、20日均线
    # df1.set_index("日期")['收盘'].plot()
    # df1.set_index("日期")['收盘'].rolling(5).mean().plot()
    # df1.set_index("日期")['收盘'].rolling(20).mean().plot()

    # 根据 df1 计算 EMA20
    # df1['EMA20'] = df1['收盘'].ewm(span=20, min_periods=0, adjust=False, ignore_na=False).mean()

    # 计算 df1 的 MACD 指标
    # exp1 = df1['收盘'].ewm(span=12, adjust=False).mean()
    # exp2 = df1['收盘'].ewm(span=26, adjust=False).mean()
    # df1['MACD'] = exp1 - exp2
    # df1['Signal line'] = df1['MACD'].ewm(span=9, adjust=False).mean()

    # 计算并绘制布林指标，计算方法参考百度百科
    # df1['former 30 days rolling Close mean'] = df1['收盘'].rolling(20).mean()
    # df1['upper bound'] = df1['former 30 days rolling Close mean'] + \
    #                      2 * df1['收盘'].rolling(20).std()  # 在这里我们取20天内的标准差
    # df1['lower bound'] = df1['former 30 days rolling Close mean'] - \
    #                      2 * df1['收盘'].rolling(20).std()
    # plt.rcParams['font.sans-serif'] = ['Songti SC']
    # df1.set_index("日期")[['收盘', 'former 30 days rolling Close mean', 'upper bound', 'lower bound']].plot(
    #     figsize=(16, 6))
    # plt.show()

    # 将 df1 的索引设置为日期，将 df1 数据向后移动一天
    # df1.set_index('日期').shift(1)

    # 将 df1 的索引设置为日期，并将全部日期向后移动一天
    # df = df1.set_index('日期').shift(freq='D')

    # 按周对 df1 进行重采样，保留每周最后一个数据
    # df = df1.set_index('日期').resample('W').last()

    # 按月对 df1 进行重采样，保留每月最后一个数据
    # df = df1.set_index('日期').resample('ME').last()

    # 按日对 df2 进行重采样，保留每天最后一个数据
    # df = df2.set_index('时间').resample('D').last()

    # 将 df2 的 5分钟 数据改为 3分钟，缺失数据向前填充
    # df_3min = df2.set_index('时间').resample('3min').last()
    # df_3min.ffill()
    # print(df_3min)


if __name__ == '__main__':
    stock_analysis()
