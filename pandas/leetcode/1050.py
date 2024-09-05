import pandas as pd


# select actor_id, director_id
# from ActorDirector
# group by actor_id, director_id
# having count(timestamp) >= 3;
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    # actor_director['count'] = actor_director.groupby(['actor_id', 'director_id']).transform('size')
    print(df)

    df = df.loc[df['count'] >= 3]
    print(df)
    return df[['actor_id', 'director_id']]


if __name__ == '__main__':
    data = [[1, 1, 0],
            [1, 1, 1],
            [1, 1, 2],
            [1, 2, 3],
            [1, 2, 4],
            [2, 1, 5],
            [2, 1, 6]]

    ActorDirector = (pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp'])
                     .astype({'actor_id': 'int64', 'director_id': 'int64', 'timestamp': 'int64'}))

    res = actors_and_directors(ActorDirector)
    # print(res)
