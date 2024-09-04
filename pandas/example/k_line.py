import pandas as pd
import matplotlib.pyplot as plt
import datetime
import mplfinance as mpf

'''
制作K线图
'''


def make_k_line():
    path1 = '../../data/stock/000001_daily.csv'
    path2 = '../../data/stock/000001_5min.csv'
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)

    # 将 df1 和 df2 的 日期 列转换为 pandas 支持的时间格式
    df1['日期'] = pd.to_datetime(df1['日期'])
    df2['时间'] = pd.to_datetime(df2['时间'])

    # 筛选 df1 中'日期','开盘','最高','最低','收盘','成交量'几列，并命名为新数据框 df_new
    df_new = df1[['日期', '开盘', '最高', '最低', '收盘', '成交量']]
    # print(df_new.head())

    # 将 df_new 的列名修改为 'Date','Open','High','Low','Close','Volume'
    df_new.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    # print(df_new.head())

    # 将 df_new 的索引列修改为 Date 列
    df_new.set_index(["Date"], inplace=True)
    # print(df_new.head())

    # 根据 df_new 绘制日线级K线，mplfinance 格式固定。
    # mpf.plot(df_new, type='line', mav=(5, 10, 15))

    # 添加5日、10日、15日移动均线，添加成交量
    # mpf.plot(df_new, type='line', mav=(5, 10, 15), volume=True)

    # 生成蜡烛图
    # df2_new = df2[(df2['时间'] > '2021-08-03 09:35:00') & (df2['时间'] < '2021-08-03 15:00:00')]
    # df2_new = df2_new[['时间', '开盘', '最高', '最低', '收盘', '成交量']]
    # df2_new.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    # df2_new.set_index(["Date"], inplace=True)
    # mpf.plot(df2_new, type='candle', mav=(3, 6, 9), volume=True)

    # 使用 df2 数据，筛选 8月3日-8月4日的数据，制作蜡烛图并展示非交易时间区间
    # df_new = df2[(df2['时间'] > '2021-08-03 9:00:00') & (df2['时间'] < '2021-08-04 15:00:00')]
    # df_new = df_new[['时间', '开盘', '最高', '最低', '收盘', '成交量']]
    # df_new.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    # df_new.set_index(["Date"], inplace=True)
    # mpf.plot(df_new, type='candle', show_nontrading=True, volume=True)


if __name__ == '__main__':
    make_k_line()
