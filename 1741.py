import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby(['emp_id', 'event_day']).agg({'in_time': "sum", 'out_time': 'sum'}).reset_index()
    df['total_time'] = df['out_time'] - df['in_time']
    df = df.astype({'total_time': 'int64'})
    df.rename(columns={'event_day': 'day'}, inplace=True)
    print(df)
    return df[['day', 'emp_id', 'total_time']]


if __name__ == '__main__':
    data = [['1', '2020-11-28', '4', '32'],
            ['1', '2020-11-28', '55', '200'],
            ['1', '2020-12-3', '1', '42'],
            ['2', '2020-11-28', '3', '33'],
            ['2', '2020-12-9', '47', '74']]

    Employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype(
        {'emp_id': 'Int64', 'event_day': 'datetime64[ns]', 'in_time': 'Int64', 'out_time': 'Int64'})

    res = total_time(Employees)
    print(res)
