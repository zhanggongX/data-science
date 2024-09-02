import pandas as pd
import os

'''
pandas 读取 csv 数据
'''


def read_csv_test():
    csv_data_path = '../../data/某招聘网站数据.csv'

    # 读取CSV文件
    df = pd.read_csv(csv_data_path)

    # 读取前20行
    df = pd.read_csv(csv_data_path, nrows=20)

    # 跳过前20行
    df = pd.read_csv(csv_data_path, skiprows=[i for i in range(1, 21)])

    # 读取指定行，奇数行
    df = pd.read_csv(csv_data_path, skiprows=lambda x: (x != 0 and not x % 2))

    # 读取指定的列
    df = pd.read_csv(csv_data_path, usecols=[0, 2, 4])

    # 指定列名读取
    df = pd.read_csv(csv_data_path, usecols=['positionId', 'positionName', 'salary'])

    # 指定列匹配读取
    use_cols = ['positionId', 'test', 'positionName', 'test1', 'salary']
    df = pd.read_csv(csv_data_path, usecols=lambda x: x in use_cols)

    # 读取时设置索引
    df = pd.read_csv(csv_data_path, index_col=['positionId'])

    # 读取时设置标题
    data = pd.read_csv(csv_data_path, usecols=[0, 1, 17], header=0, names=['ID', '岗位名称', '薪资'])

    # 读取并处理缺失值
    # 读取当前目录下 某招聘网站数据.csv 文件，并不将缺失值标记为 NA
    df = pd.read_csv(csv_data_path, keep_default_na=False)
    # 读取当前目录下 某招聘网站数据.csv 文件，并将[]标记为缺失值
    df = pd.read_csv(csv_data_path, na_values=['[]'])
    # 读取当前目录下 某招聘网站数据.csv 文件，但不处理缺失值
    df = pd.read_csv(csv_data_path, na_filter=False)

    # 读取时设置格式
    df = pd.read_csv(csv_data_path, dtype={'positionId': str, 'companyId': str})  # 指定字符串格式
    df = pd.read_csv(csv_data_path, parse_dates=['createTime'])  # 指定时间格式

    # 分块读取
    for chunk in pd.read_csv(csv_data_path, chunksize=10):
        print(chunk)

    # 循环读取数据
    path = '../../data/'
    files_names = os.listdir(path)
    files_names = [f for f in files_names if f.lower().endswith(".xlsx")]
    df_list = []
    for filename in files_names:
        df_list.append(pd.read_excel(path + filename))
    df = pd.concat(df_list)

    print(df)


if __name__ == '__main__':
    read_csv_test()
