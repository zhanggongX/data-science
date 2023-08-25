import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    for x in accounts.index:
        if accounts.loc[x, 'income'] < 20000:
            accounts.loc[x, 'category'] = 'Low Salary'
        elif accounts.loc[x, 'income'] > 50000:
            accounts.loc[x, 'category'] = 'Average Salary'
        else:
            accounts.loc[x, 'category'] = 'High Salary'
    df = accounts.groupby(['category']).agg({'account_id': 'count'}).reset_index()
    df.rename(columns={'account_id': 'accounts_count'}, inplace=True)

    df_category = pd.DataFrame([['Low Salary'], ['Average Salary'], ['High Salary']], columns=['category'])
    df = pd.merge(df_category, df, on='category', how='left')
    df.fillna({'accounts_count': 0}, inplace=True)
    df = df.astype({'accounts_count': 'int64'})
    print(df)


if __name__ == '__main__':
    data = [[3, 108939],
            [2, 12747],
            [8, 87709],
            [6, 91796]]
    Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id': 'Int64', 'income': 'Int64'})

    res = count_salary_categories(Accounts)
    print(res)
