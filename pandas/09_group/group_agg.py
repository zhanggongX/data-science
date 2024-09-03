import pandas as pd
import numpy as np

'''
分组聚合
'''


def test_group_agg():
    path = '../../data/某招聘网站数据.csv'
    df = pd.read_csv(path)

    # 计算各区(district)的薪资(salary)均值
    # df = df[['district', 'salary']].groupby('district').mean()
    # df = df.groupby("district")['salary'].mean()

    # 按照上面要求进行分组，但不使用 district 做为索引
    # df = df.groupby("district", as_index=False)['salary'].mean()

    # 计算并提取平均薪资最高的区
    # df = df[['district', 'salary']].groupby(by='district').mean().sort_values('salary', ascending=False).head(1)

    # 计算不同行政区(district)，不同规模公司(companySize)出现的次数
    # df = pd.DataFrame(df.groupby("district")['companySize'].value_counts())
    # df = df.groupby(by=['district','companySize']).size()

    # 计算不同行政区(district)，不同规模公司(companySize)出现的次数, 索引名修改为 district -> 行政区 companySize -> 公司规模
    # df = pd.DataFrame(df.groupby("district")['companySize'].value_counts()).rename_axis(["行政区", "公司规模"])

    # 统计每个区出现的公司数量
    # df = df.groupby("district")['companySize'].count()


    print(df)


if __name__ == '__main__':
    test_group_agg()
