'''
select q.query_name,
round(avg(q.rating/q.position), 2) quality,
round(sum(if(q.rating < 3, 100, 0)) / count(q.rating), 2) poor_query_percentage
from Queries q where q.query_name is not null
group by q.query_name;
'''

import pandas as pd


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating'] / queries['position']
    return queries.groupby('query_name').agg(
        quality=('quality', lambda x: round(x.mean(), 2)),
        poor_query_percentage=('rating', lambda x: round((x < 3).sum() / len(x), 2))).reset_index()


if __name__ == '__main__':
    data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1],
            ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
    queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype(
        {'query_name': 'object', 'result': 'object', 'position': 'Int64', 'rating': 'Int64'})

    print(queries_stats(queries))
