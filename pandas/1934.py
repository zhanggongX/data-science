import pandas as pd


# select s.user_id,
# round(sum(if (c.action='confirmed', 1.00, 0.00)) / count(s.user_id), 2) confirmation_rate
# from Signups s left join Confirmations c on s.user_id = c.user_id
# group by s.user_id;
def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(signups, confirmations, how='left', on='user_id')
    df = df.groupby('user_id')
    ans = df.agg(confirmation_rate=('action', lambda x: (x == 'confirmed').mean().round(2)))
    return ans.reset_index()


if __name__ == '__main__':
    data = [[3, '2020-03-21 10:16:13'], [7, '2020-01-04 13:57:59'], [2, '2020-07-29 23:09:44'],
            [6, '2020-12-09 10:39:37']]
    signups = pd.DataFrame(data, columns=['user_id', 'time_stamp']).astype(
        {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]'})

    data = [[3, '2021-01-06 03:30:46', 'timeout'], [3, '2021-07-14 14:00:00', 'timeout'],
            [7, '2021-06-12 11:57:29', 'confirmed'], [7, '2021-06-13 12:58:28', 'confirmed'],
            [7, '2021-06-14 13:59:27', 'confirmed'], [2, '2021-01-22 00:00:00', 'confirmed'],
            [2, '2021-02-28 23:59:59', 'timeout']]
    confirmations = pd.DataFrame(data, columns=['user_id', 'time_stamp', 'action']).astype(
        {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]', 'action': 'object'})

    res = confirmation_rate(signups, confirmations)
    print(res)
