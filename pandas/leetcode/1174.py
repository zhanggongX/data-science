'''
with t as
(select d.*, rank() over(partition by customer_id order by order_date) rnk from Delivery d)

select round(count(if(order_date = customer_pref_delivery_date, 1, null)) * 100 / count(delivery_id), 2) immediate_percentage
from t
where t.rnk = 1;
'''
import numpy as np
import pandas as pd


def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # 解法一：
    # delivery = delivery.assign(rnk=delivery.groupby('customer_id')['order_date'].rank(method='first'))
    # df = delivery[delivery['rnk'] == 1]
    # count1 = 0
    # count2 = 0
    # for idx, row in df.iterrows():
    #     if row['order_date'] == row['customer_pref_delivery_date']:
    #         count1 += 1
    #     count2 += 1
    # immediate_percentage = round(count1 / count2 * 100, 2)
    # res = pd.DataFrame([{'immediate_percentage': immediate_percentage}])
    # return res

    # 解法二：
    # delivery = delivery.sort_values(by='order_date', ascending=True).drop_duplicates(subset='customer_id', keep='first')
    # delivery['instant'] = np.where(delivery['order_date'] == delivery['customer_pref_delivery_date'], 100, 0)
    # return pd.DataFrame({'immediate_percentage': [round(delivery['instant'].mean(), 2)]})

    # 解法三：
    delivery.sort_values(by='order_date', inplace=True)  # 对日期进行升序排序
    delivery.drop_duplicates(subset='customer_id', keep='first', inplace=True)  # 去除顾客号相同的并保留第一个记录
    equal = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]  # 找到即时订单
    bili = round(len(equal) / len(delivery) * 100, 2)
    return pd.DataFrame({'immediate_percentage': [bili]})


if __name__ == '__main__':
    data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-12'],
            [4, 3, '2019-08-24', '2019-08-24'], [5, 3, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13'],
            [7, 4, '2019-08-09', '2019-08-09']]
    delivery = pd.DataFrame(data,
                            columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype(
        {'delivery_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]',
         'customer_pref_delivery_date': 'datetime64[ns]'})

    print(immediate_food_delivery(delivery))
