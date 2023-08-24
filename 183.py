import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # return customers
    df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    # df[df['customerId'] != null]
    print(df)
    df_new = df[df['customerId'].isnull()][['name']]
    print(df_new)
    df_new.rename(columns={'name': 'customers'}, inplace=True)
    return df_new


if __name__ == '__main__':
    data = [[1, 'Joe'],
            [2, 'Henry'],
            [3, 'Sam'],
            [4, 'Max']]
    Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[1, 3],
            [2, 1]]
    Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})
    res = find_customers(Customers, Orders)
    print(res)
