import pandas as pd


# select count(*) as rich_count from (select customer_id from Store where amount > 500 group by customer_id) t1;
def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_customers = store[store["amount"] > 500]
    # rich_count = len(set(rich_customers['customer_id']))
    rich_count = rich_customers["customer_id"].nunique()
    res = pd.DataFrame({"rich_count": [rich_count]})
    return res


if __name__ == "__main__":
    store_data = {
        'bill_id': [6, 8, 4, 11, 13],
        'customer_id': [1, 1, 2, 3, 3],
        'amount': [549, 834, 394, 657, 257]
    }
    pd_store = pd.DataFrame(store_data)
    print(pd_store)

    pd_res = count_rich_customers(pd_store)
    print(pd_res)
