import pandas as pd


# with t as (select product_id, min(year) first_year from Sales group by product_id)
#
# select s.product_id, s.year as first_year, s.quantity, s.price
# from Sales s right join t on s.product_id = t.product_id and s.year = t.first_year;
def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('product_id', as_index=False)['year'].min().rename(columns={'year': 'first_year'})
    df = df.merge(sales, left_on=['product_id', 'first_year'], right_on=['product_id', 'year'], how='left')
    return df[['product_id', 'first_year', 'quantity', 'price']]


if __name__ == '__main__':
    data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
    sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype(
        {'sale_id': 'Int64', 'product_id': 'Int64', 'year': 'Int64', 'quantity': 'Int64', 'price': 'Int64'})
    data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
    product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype(
        {'product_id': 'Int64', 'product_name': 'object'})

    res = sales_analysis(sales, product)
    print(res)
