import pandas as pd

# select machine_id, round(avg(times), 3) as processing_time
# from
# (select
# machine_id, process_id, max(timestamp) - min(timestamp) times
# from Activity
# group by machine_id, process_id) t1
# group by t1.machine_id;

# select machine_id, round(sum(
#     case when activity_type = 'end'
#     then timestamp
#     else -timestamp
#     end) / count(distinct process_id), 3) as processing_time
# from activity
# group by machine_id
def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    end_time = activity.loc[activity.activity_type == 'end'].groupby('machine_id').timestamp.sum().reset_index()
    start_time = activity.loc[activity.activity_type == 'start'].groupby('machine_id').timestamp.sum().reset_index()
    end_time['processing_time'] = round((end_time.timestamp - start_time.timestamp) / activity.process_id.nunique(), 3)
    return end_time[['machine_id', 'processing_time']]

if __name__ == '__main__':
    data = [[0, 0, 'start', 0.712],
            [0, 0, 'end', 1.52],
            [0, 1, 'start', 3.14],
            [0, 1, 'end', 4.12],
            [1, 0, 'start', 0.55],
            [1, 0, 'end', 1.55],
            [1, 1, 'start', 0.43],
            [1, 1, 'end', 1.42],
            [2, 0, 'start', 4.1],
            [2, 0, 'end', 4.512],
            [2, 1, 'start', 2.5],
            [2, 1, 'end', 5]]

    activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype(
        {'machine_id': 'Int64', 'process_id': 'Int64', 'activity_type': 'object', 'timestamp': 'Float64'})

    res = get_average_time(activity)
    print(res)