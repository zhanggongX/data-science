import pandas as pd


def do_drop():
    missing_values = ['n/a', 'na', '--']
    df = pd.read_csv('test.csv', na_values=missing_values)
    # DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    # print(df)
    # print(df['NUM_BEDROOMS'])
    # print(df['NUM_BEDROOMS'].isnull())

    # df_1 = df.dropna()
    # print(df_1.to_string())

    # df.dropna(inplace=True)
    # print(df)

    # df.dropna(subset=['ST_NUM'], inplace=True)
    # print(df)

    # df.fillna('fill_na', inplace=True)
    # print(df)

    # df['PID'].fillna('fill_pid', inplace=True)
    # print(df)

    # mean 列的平均数, median 中位数, mode 众数
    x = df['ST_NUM'].mean()
    y = df['ST_NUM'].median()
    z = df['ST_NUM'].mode()
    df['ST_NUM'].fillna(x, inplace=True)
    print(df)


data = {
    "Date": ['2020/12/01', '2020/12/02', '20201226'],
    "duration": [50, 40, 45]
}

person = {
    "name": ['Google', 'tiktok', 'tiktok', 'alibaba'],
    "age": [50, 40, 50, 12345]  # 12345 年龄数据是错误的
}


def do_drop_error():
    # df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
    # df['Date'] = pd.to_datetime(df['Date'])
    # df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # df['Date'] = pd.to_datetime(df['Date'], format='ISO8601')
    # print(df)

    df_p = pd.DataFrame(person)
    # df_p.loc[2, 'age'] = 30
    # print(df_p)
    # for x in df_p.index:
    #     if df_p.loc[x, 'age'] >= 40:
    #         df_p.loc[x, 'age'] = 20
    # print(df_p)
    #
    # for x in df_p.index:
    #     if df_p.loc[x, 'age'] >= 30:
    #         df_p.drop(x, inplace=True)
    # print(df_p)

    print(df_p.duplicated(subset=['name']))
    print(df_p)
    # df_p.drop_duplicates(inplace=True)
    df_p.sort_values(by='age', ascending=False, inplace=True)
    print(df_p)
    df_p.drop_duplicates(subset=['name'], inplace=True)
    print(df_p)


if __name__ == '__main__':
    # do_drop()
    do_drop_error()
