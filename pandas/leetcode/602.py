import pandas as pd


# with t as
# (select r.requester_id, r.accepter_id from RequestAccepted r
# union all
# select r.accepter_id requester_id, r.requester_id accepter_id from RequestAccepted r)
#
# select t.requester_id id, count(t.accepter_id) num from t group by t.requester_id order by count(t.accepter_id) desc limit 1;
def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df = request_accepted.rename(columns={'requester_id': 'accepter_id', 'accepter_id': 'requester_id'})
    df = pd.concat([request_accepted, df])
    df = df.groupby('requester_id').agg({'accepter_id': 'count'}).reset_index()
    df.rename(columns={'accepter_id': 'num', 'requester_id': 'id'}, inplace=True)
    return df.sort_values('num', ascending=False).head(1)


if __name__ == '__main__':
    data = [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']]
    request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype(
        {'requester_id': 'Int64', 'accepter_id': 'Int64', 'accept_date': 'datetime64[ns]'})

    res = most_friends(request_accepted)
    print(res)
