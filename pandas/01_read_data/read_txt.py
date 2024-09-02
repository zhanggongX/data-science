import pandas as pd

'''
pandas 读取 txt 数据
'''


def test_read_txt():
    txt_file_path = '../../data/Titanic.txt'
    txt_file_path250 = '../../data/TOP250.txt'

    data = pd.read_table(txt_file_path)

    # 指定编码读取
    data = pd.read_table(txt_file_path250, encoding='gb18030')
    print(data)


if __name__ == '__main__':
    test_read_txt()
