'''
select
date_format(trans_date, '%Y-%m') month, country,
count(amount) as trans_count,
sum(case when state='approved' then 1 else 0 end) as approved_count,
sum(amount) as trans_total_amount,
sum(case when state='approved' then amount else 0 end) as approved_total_amount
from Transactions group by date_format(trans_date, '%Y%-%m'), country;
'''
import numpy as np
import pandas as pd


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    return transactions.groupby(['month', 'country']).agg(
        trans_count=('id', 'count'),
        approved_count=('state', lambda x: x.eq('approved').sum()),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('amount', lambda x: sum(x[transactions["state"] == "approved"]))
    ).reset_index()


if __name__ == '__main__':
    data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'],
            [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
    transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype(
        {'id': 'Int64', 'country': 'object', 'state': 'object', 'amount': 'Int64', 'trans_date': 'datetime64[ns]'})

    print(monthly_transactions(transactions))
