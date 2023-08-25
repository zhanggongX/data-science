import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # for x in accounts.index:
    #     if accounts.loc[x, 'income'] < 20000:
    #         accounts.loc[x, 'category'] = 'Low Salary'
    #     elif accounts.loc[x, 'income'] > 50000:
    #         accounts.loc[x, 'category'] = 'High Salary'
    #     else:
    #         accounts.loc[x, 'category'] = 'Average Salary'
    # df = accounts.groupby(['category']).agg({'account_id': 'count'}).reset_index()
    # df.rename(columns={'account_id': 'accounts_count'}, inplace=True)
    # print(df)
    #
    # df_category = pd.DataFrame([['Low Salary'], ['Average Salary'], ['High Salary']], columns=['category'])
    # df = pd.merge(df_category, df, on='category', how='left')
    # df.fillna({'accounts_count': 0}, inplace=True)
    # df = df.astype({'accounts_count': 'int64'})
    # print(df)
    # return df

    low_count = (accounts['income'] < 20000).sum()
    average_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_count = (accounts['income'] > 50000).sum()

    ans = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_count, average_count, high_count]
    })

    return ans


if __name__ == '__main__':
    data = [[3, 108939],
            [2, 12747],
            [8, 87709],
            [6, 91796]]
    Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id': 'Int64', 'income': 'Int64'})

    res = count_salary_categories(Accounts)
    print(res)
