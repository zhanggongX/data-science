import pandas as pd

'''
SELECT 
    s.product_id, p.product_name
FROM 
    sales s
LEFT JOIN 
    product p 
ON 
    s.product_id = p.product_id
GROUP BY 
    s.product_id
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31';
'''


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = product.merge(sales, on='product_id', how='left')
    df = df.groupby(['product_id', 'product_name'], as_index=False).agg(min_date=('sale_date', 'min'),
                                                                        max_date=('sale_date', 'max'))
    df = df[(df['min_date'] >= '2019-01-01') & (df['max_date'] <= '2019-03-31')]
    return df[['product_id', 'product_name']]


if __name__ == '__main__':
    data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
    product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype(
        {'product_id': 'Int64', 'product_name': 'object', 'unit_price': 'Int64'})
    data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800],
            [3, 3, 4, '2019-05-13', 2, 2800]]
    sales = pd.DataFrame(data,
                         columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype(
        {'seller_id': 'Int64', 'product_id': 'Int64', 'buyer_id': 'Int64', 'sale_date': 'datetime64[ns]',
         'quantity': 'Int64', 'price': 'Int64'})

    res = sales_analysis(product, sales)
    print(res)
