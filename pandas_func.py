import pandas as pd


def pandas_read():
    df = pd.read_csv('test.csv')
    print(df)


if __name__ == '__main__':
    pandas_read()
