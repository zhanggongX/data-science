import pandas as pd


# select transaction_date,
# sum(if(amount%2 = 1, amount, 0)) as odd_sum,
# sum(if(amount%2 = 0, amount, 0)) as even_sum
# from transactions
# group by transaction_date order by transaction_date;
def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    data = transactions.groupby('transaction_date').agg(
        odd_sum=('amount', lambda x: x[transactions['amount'] % 2 != 0].sum()),
        even_sum=('amount', lambda x: x[transactions['amount'] % 2 == 0].sum())).reset_index()
    data['odd_sum'] = data['odd_sum'].fillna(0)
    data['even_sum'] = data['even_sum'].fillna(0)
    return data.sort_values('transaction_date')


if __name__ == '__main__':
    data = [[1, 150, '2024-07-01'],
            [2, 200, '2024-07-01'],
            [3, 75, '2024-07-01'],
            [4, 300, '2024-07-02'],
            [5, 50, '2024-07-02'],
            [6, 120, '2024-07-03']]
    transactions = pd.DataFrame(data, columns=["transaction_id", "amount", "transaction_date"])

    # 确保日期列是日期类型
    transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])

    res = sum_daily_odd_even(transactions)
    print(res)
