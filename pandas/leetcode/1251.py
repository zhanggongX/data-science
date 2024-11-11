'''
select p.product_id, ifnull(round(sum(p.price * u.units) / sum(u.units) , 2), 0) as average_price from
Prices p
left join UnitsSold u
on p.product_id = u.product_id and p.start_date <= u.purchase_date and p.end_date >= u.purchase_date
group by p.product_id;
'''

import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, on='product_id', how='left')
    df = df[(df['purchase_date'] >= df['start_date']) & (df['purchase_date'] <= df['end_date'])]

    result = df.groupby('product_id').agg(average_price=('units', lambda x: ((x * df['price']).sum() / x.sum()).round(2))).reset_index()

    all_products = prices['product_id'].unique()
    res = pd.DataFrame(all_products, columns=['product_id'])
    return res.merge(result, on='product_id', how='left').fillna(0)


if __name__ == '__main__':
    data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20],
            [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
    prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype(
        {'product_id': 'Int64', 'start_date': 'datetime64[ns]', 'end_date': 'datetime64[ns]', 'price': 'Int64'})
    data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
    units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype(
        {'product_id': 'Int64', 'purchase_date': 'datetime64[ns]', 'units': 'Int64'})

    print(average_selling_price(prices, units_sold))
