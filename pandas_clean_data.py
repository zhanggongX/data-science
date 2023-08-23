import pandas as pd


def do_drop():
    missing_values = ['n/a', 'na', '--']
    df = pd.read_csv('test.csv', na_values=missing_values)
    # DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    # print(df)
    # print(df['NUM_BEDROOMS'])
    # print(df['NUM_BEDROOMS'].isnull())
    df_1 = df.dropna()
    print(df_1.to_string())
    df.dropna(inplace=True)
    print(df)


if __name__ == '__main__':
    do_drop()
