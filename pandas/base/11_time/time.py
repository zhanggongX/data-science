import pandas as pd
import numpy as np

def test_time():
    # 生成当前时间
    df = pd.Timestamp('now')

    # 生成指定时间范围
    df = pd.date_range('2021-01-01', '2021-09-11')

    # 生成指定间隔时间
    df = pd.date_range("2021-01-01", periods=10)

    # 使用 pandas 从 2021年1月1日开始，按周生成 7 周日期
    df = pd.date_range("2021-01-01", periods=7, freq="W")

    # 使用 pandas 按天生成 2021年1月1日 至 2021年9月1日的全部工作日日期
    df = pd.bdate_range('2021-01-01', '2021-09-11')

    # 使用 pandas 计算 2021年2月14日 距离今天相差多少天
    df = (pd.Timestamp('now') - pd.to_datetime('2021-02-14')).days

    # 使用 pandas 计算 2021年9月1日13点14分 距离今天相差多少小时
    df = (pd.Timestamp('now') - pd.to_datetime('2021-09-01 13:14:00')) / np.timedelta64(1, 'h')

    # 将现在的时间减去一天，并格式化为 xx年xx月xx日 xx时xx分xx秒
    df = (pd.Timestamp('now') - pd.to_timedelta('1 day'))

    # 时间格式化
    df = (pd.Timestamp('now') - pd.to_timedelta('1 day')).strftime("%Y年%m月%d日-%H时%M分%S秒")

    print(df)


if __name__ == '__main__':
    test_time()
