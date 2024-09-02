from itertools import groupby

import pandas as pd

'''
select customer_id 
from Customer 
group by customer_id 
having count(distinct product_key) = (select count(*) from Product);
'''


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    df = df[df['product_key'] == len(product)]
    return df[['customer_id']]


if __name__ == '__main__':
    data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
    customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype(
        {'customer_id': 'Int64', 'product_key': 'Int64'})
    data = [[5], [6]]
    product = pd.DataFrame(data, columns=['product_key']).astype({'product_key': 'Int64'})

    res = find_customers(customer, product)
    print(res)
