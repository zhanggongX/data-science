import pandas as pd


def food_deliver(deliver: pd.DataFrame) -> pd.DataFrame:
    return deliver


if __name__ == "__main__":
    deliver_table = {
        'deliver_id': [1, 2, 3, 4, 5, 6],
        'customer_id': [1, 5, 1, 3, 4, 2],
        'order_date': ["2019-08-01", "2019-08-02", "2019-08-11", "2019-08-24", "2019-08-21", "2019-08-11"],
        'customer_perf_deliver_date': ["2019-08-02", "2019-08-02", "2019-08-11", "2019-08-26", "2019-08-22",
                                       "2019-08-13"]
    }
    deliver_pd = pd.DataFrame(deliver_table)
    deliver_pd.set_index('deliver_id', inplace=True)
    print(deliver_pd)
    res_pd = food_deliver(deliver_pd)
    print(res_pd)
