import pandas as pd


# def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:with t as
# (select id, visit_date, people, row_number() over(order by id) rnk from Stadium where people >= 100),
# t1 as
# (select id, visit_date, people, (id - rnk) id1 from t),
# t2 as
# (select id1 from t1 group by id1 having count(id1) >= 3)
#
# select id, visit_date, people from t1 where t1.id1 in (select * from t2);
def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    df = stadium[stadium['people'] >= 100]
    df.sort_values('id', inplace=True)
    df['rnk'] = df['id'].rank(method='dense')
    df['id1'] = df['id'] - df['rnk']

    df['count'] = df.groupby('id1')['id1'].transform('count')

    df = df.loc[df['count'] >= 3]
    return df[['id', 'visit_date', 'people']]


if __name__ == '__main__':
    data = [[1, '2017-01-01', 10], [2, '2017-01-02', 109], [3, '2017-01-03', 150], [4, '2017-01-04', 99],
            [5, '2017-01-05', 145], [6, '2017-01-06', 1455], [7, '2017-01-07', 199], [8, '2017-01-09', 188]]
    stadium = pd.DataFrame(data, columns=['id', 'visit_date', 'people']).astype(
        {'id': 'Int64', 'visit_date': 'datetime64[ns]', 'people': 'Int64'})

    res = human_traffic(stadium)
    print(res)
