import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values('user_id')


if __name__ == '__main__':
    data = [[1, 'aLice'], [2, 'bOB']]
    Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id': 'Int64', 'name': 'object'})

    res = fix_names(Users)
    print(res)
