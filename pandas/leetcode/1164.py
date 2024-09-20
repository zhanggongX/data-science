'''
select t1.product_id, ifnull(t2.new_price, 10) as price
from (select product_id from Products group by product_id) t1
         left join
     (select *
      from Products p
      where (product_id, change_date) in
            (select product_id, max(change_date) last_change_date
             from Products
             where change_date <= '2019-08-16'
             group by product_id)) t2 on t1.product_id = t2.product_id;
'''

import pandas as pd


def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    # 筛选日期
    df1 = products[products['change_date'] <= '2019-08-16']
    # 保留(product_id,最后日期)
    df1 = df1.groupby('product_id', as_index=False).agg({'change_date': 'max'})
    # 使用元组 isin 判断
    df2 = products[products[['product_id', 'change_date']].apply(tuple, axis=1).isin(df1.apply(tuple, axis=1))]

    df = products[['product_id']].drop_duplicates()
    df = df.merge(df2, on='product_id', how='left').fillna(10)
    return df[['product_id', 'new_price']].rename(columns={'new_price': 'price'})



if __name__ == '__main__':
    data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'],
            [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
    products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype(
        {'product_id': 'Int64', 'new_price': 'Int64', 'change_date': 'datetime64[ns]'})

    print(price_at_given_date(products))
