import pandas as pd


def food_deliver(deliver: pd.DataFrame) -> pd.DataFrame:
    now = (deliver['order_date'] == deliver['customer_pref_delivery_date']).sum()
    count = len(deliver)
    pce = round(100 * now / count, 2)
    return pd.DataFrame({'immediate_percentage': [pce]})


if __name__ == "__main__":
    data = [[1, 1, '2019-08-01', '2019-08-02'],
            [2, 5, '2019-08-02', '2019-08-02'],
            [3, 1, '2019-08-11', '2019-08-11'],
            [4, 3, '2019-08-24', '2019-08-26'],
            [5, 4, '2019-08-21', '2019-08-22'],
            [6, 2, '2019-08-11', '2019-08-13']]
    Delivery = (pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date'])
                .astype({'delivery_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]',
                         'customer_pref_delivery_date': 'datetime64[ns]'}))
    res_pd = food_deliver(Delivery)
    print(res_pd)
