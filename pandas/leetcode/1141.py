import pandas as pd

'''
select activity_date as day, count(distinct user_id) as active_users  
from Activity 
where activity_date > date_sub('2019-07-27', interval 30 day) 
and activity_date <= '2019-07-27' 
group by activity_date;
'''


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    time = (pd.Timestamp('2019-07-27') - pd.to_timedelta('30 day')).strftime("%Y-%m-%d")
    df = activity[(activity['activity_date'] <= '2019-07-27') & (activity['activity_date'] > time)]
    df = df.groupby('activity_date').agg(active_users=('user_id', 'nunique')).rename_axis('day').reset_index()
    return df


if __name__ == '__main__':
    data = [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'],
            [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'],
            [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'],
            [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'],
            [3, 2, '2019-07-21', 'end_session'], [4, 3, '2019-06-25', 'open_session'],
            [4, 3, '2019-06-25', 'end_session']]
    activity = pd.DataFrame(data, columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype(
        {'user_id': 'Int64', 'session_id': 'Int64', 'activity_date': 'datetime64[ns]', 'activity_type': 'object'})

    print(user_activity(activity))
