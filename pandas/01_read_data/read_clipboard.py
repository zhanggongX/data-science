import pandas as pd

'''
pandas 读取 剪切板 数据

out:
Empty DataFrame
Columns: [有时，我们想快速读取一些数据，又不想保存数据再读取。]
Index: []
'''


def test_read_clipboard():
    df = pd.read_clipboard()
    print(df)


if __name__ == '__main__':
    test_read_clipboard()
