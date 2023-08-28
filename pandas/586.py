import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby(['customer_number']).agg({'order_number': 'count'}).reset_index()
    df.sort_values(by='order_number', ascending=False, inplace=True)
    print(df)
    return df.head(1)[['customer_number']]


if __name__ == '__main__':
    data = [[1, 1],
            [2, 2],
            [3, 3],
            [4, 3]]
    orders_df = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype(
        {'order_number': 'Int64', 'customer_number': 'Int64'})

    res = largest_orders(orders_df)
    print(res)
