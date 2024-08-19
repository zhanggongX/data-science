import pandas as pd


# select customer_number
# from (select customer_number, count(order_number) order_numbers from Orders group by customer_number) t
# order by order_numbers desc
# limit 1
if __name__ == '__main__':

    data = [[1, 1], [2, 2], [3, 3], [4, 3]]
    orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype(
        {'order_number': 'Int64', 'customer_number': 'Int64'})

    df = orders.groupby('customer_number').count()
    df.reset_index(inplace=True)
    df.sort_values(by=['order_number'], ascending=False, inplace=True)
    df = df.head(1)[['customer_number']]
    print(df)