import pandas as pd

'''
数据探索和描述性统计分析
'''


def test_search_data():
    top_university_file_path = '../../data/2020年中国大学排名.xlsx'
    df = pd.read_excel(top_university_file_path)

    df = df[df['学校名称'] == '郑州大学']
    print(df)


if __name__ == '__main__':
    test_search_data()
