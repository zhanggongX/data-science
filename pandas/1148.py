import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views['yes'] = views['author_id'] == views['viewer_id']
    df = views[views['yes']]['author_id']
    df = pd.DataFrame(df)
    df.drop_duplicates(inplace=True)
    df = df.rename(columns={'author_id': 'id'})
    df.sort_values(by='id', inplace=True)
    print(df)
    return df


data = [[1, 3, 5, '2019-08-01'],
        [1, 3, 6, '2019-08-02'],
        [2, 7, 7, '2019-08-01'],
        [2, 7, 6, '2019-08-02'],
        [4, 7, 1, '2019-07-22'],
        [3, 4, 4, '2019-07-21'],
        [3, 4, 4, '2019-07-21']]
Views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
    {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})

article_views(Views)
