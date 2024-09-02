import pandas as pd


# select product_name, sumUnit unit from (
#     select product_id, sum(unit) sumUnit from Orders
#     where order_date >= '2020-02-01' and order_date <= '2020-02-29'
#     group by product_id) t1
# left join Products p on t1.product_id = p.product_id
# where sumUnit >= 100;
def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders[(orders["order_date"] >= "2020-02-01") & (orders["order_date"] <= "2020-02-29")]
    df = df.groupby("product_id").agg({"unit": "sum"}).reset_index()

    df = products.merge(df, how="left", on="product_id").fillna(0)

    return df[df["unit"] >= 100][["product_name", "unit"]]


if __name__ == '__main__':
    data = [[1, 'Leetcode Solutions', 'Book'],
            [2, 'Jewels of Stringology', 'Book'],
            [3, 'HP', 'Laptop'],
            [4, 'Lenovo', 'Laptop'],
            [5, 'Leetcode Kit', 'T-shirt']]

    products = pd.DataFrame(data, columns=['product_id', 'product_name', 'product_category']).astype(
        {'product_id': 'Int64', 'product_name': 'object', 'product_category': 'object'})

    data = [[1, '2020-02-05', 60],
            [1, '2020-02-10', 70],
            [2, '2020-01-18', 30],
            [2, '2020-02-11', 80],
            [3, '2020-02-17', 2],
            [3, '2020-02-24', 3],
            [4, '2020-03-01', 20],
            [4, '2020-03-04', 30],
            [4, '2020-03-04', 60],
            [5, '2020-02-25', 50],
            [5, '2020-02-27', 50],
            [5, '2020-03-01', 50]]
    orders = pd.DataFrame(data, columns=['product_id', 'order_date', 'unit']).astype(
        {'product_id': 'Int64', 'order_date': 'datetime64[ns]', 'unit': 'Int64'})

    res = list_products(products, orders)
    print(res)