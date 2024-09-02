import pandas as pd

'''
pandas 检查重复数据
'''


def test_check_dup_data():
    douban_top_250_path = '../../data/TOP250.xlsx'
    df = pd.read_excel(douban_top_250_path)

    # 查找全部重复值
    # df = df[df.duplicated()]

    # 删除全部的重复值
    # df = df.drop_duplicates()

    # 删除全部的重复值，但保留最后一次出现的值
    # df = df.drop_duplicates(keep='last')
    # df.to_html('out.html')


if __name__ == '__main__':
    test_check_dup_data()
