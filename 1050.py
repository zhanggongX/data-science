import pandas as pd


# select unique_id, name from Employees left join EmployeeUNI on Employees.id = EmployeeUNI.id
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    # 使用条件筛选
    # filtered_df = df.loc[df['Age'] > 25]
    #
    # print(filtered_df)

    df_new = df.loc[df['count'] >= 3]
    print(df_new)
    return df_new[['actor_id', 'director_id']]


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
