import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = (activities.groupby('sell_date').agg(
        num_sold=('product', pd.Series.nunique),
        products=('product', lambda x: ','.join(sorted(set(x)))))
          .reset_index())
    return df


if __name__ == '__main__':
    data = [['2020-05-30', 'Headphone'],
            ['2020-06-01', 'Pencil'],
            ['2020-06-02', 'Mask'],
            ['2020-05-30', 'Basketball'],
            ['2020-06-01', 'Bible'],
            ['2020-06-02', 'Mask'],
            ['2020-05-30', 'T-Shirt']]
    Activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype(
        {'sell_date': 'datetime64[ns]', 'product': 'object'})

    res = categorize_products(Activities)
    print(res)
