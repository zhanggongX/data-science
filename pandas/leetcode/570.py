import pandas as pd


# select name
# from Employee e
#  where id in
#     (select managerId
#         from Employee group by managerId
#         having count(managerId) >= 5);
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # df = employee.groupby('managerId').size().reset_index(name='manageCount')
    df = employee.groupby(['managerId'], as_index=False)['name'].count()
    df.rename(columns={'name': 'manageCount'}, inplace=True)
    print(df)
    df = df[df['manageCount'] >= 5]
    print(df)
    df = employee.merge(df, left_on='id', right_on='managerId', how='left')
    df = df[~df['manageCount'].isnull()][['name']]
    return df


if __name__ == '__main__':
    data = [[101, 'John', 'A', None],
            [102, 'Dan', 'A', 101],
            [103, 'James', 'A', 101],
            [104, 'Amy', 'A', 101],
            [105, 'Anne', 'A', 101],
            [106, 'Ron', 'B', 101]]
    Employee = (pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId'])
                .astype({'id': 'Int64', 'name': 'object', 'department': 'object', 'managerId': 'Int64'}))
    res = find_managers(Employee)
    print(res)
