import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
分组聚合
'''


def test_group_agg():
    path = '../../../data/某招聘网站数据.csv'
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

    # 将数据按照 district、salary 进行分组，并查看各分组内容
    # df = df.groupby(['district', 'salary']).groups

    # 将数据按照 district、salary 进行分组，并查看西湖区薪资为 30000 的工作
    # df = df.groupby(['district', 'salary']).get_group(('西湖区', 30000))

    # 根据 createTime 列，计算每天不同 行政区 新增的岗位数量
    # df['createTime'] = pd.to_datetime(df['createTime'])
    # df = pd.DataFrame(df.groupby([df.createTime.apply(lambda x: x.day)])['district'].value_counts()).rename_axis(["发布日", "行政区"])

    # 计算各行政区的企业领域（industryField）包含电商的总数
    # df = df.groupby("district", sort=False)["industryField"].apply(lambda x: x.str.contains("电商").sum())

    # 通过 positionName 的长度进行分组，并计算不同长度岗位名称的薪资均值
    # df = df.set_index("positionName").groupby(len)['salary'].mean();

    # 将 score 和 matchScore 的和记为总分，与 salary 列同时进行分组，并查看结果
    # df = df.groupby({'salary': '薪资', 'score': '总分', 'matchScore': '总分'}, axis=1).sum()

    # 计算不同 工作年限（workYear）和 学历（education）之间的薪资均值
    # df = pd.DataFrame(df['salary'].groupby([df['workYear'], df['education']]).mean())

    # 在原数据框 df 新增一列，数值为该区的平均薪资水平
    # df['该区平均工资'] = df[['district', 'salary']].groupby(by='district').transform('mean')

    # 提取平均工资小于 30000 的行政区的全部数据
    # df = df.groupby('district').filter(lambda x: x['salary'].mean() < 30000)

    # 对杭州市各区公司数量进行分组，并使用柱状图进行可视化
    # plt.rcParams['figure.dpi'] = 300
    # plt.rcParams['font.sans-serif'] = ['Songti SC']
    # df.groupby("district")['positionName'].count().plot(kind='bar', figsize=(4, 2), color='#5172F0', fontsize=6)
    # plt.ylabel("公司数量", fontsize=8)
    # plt.xlabel("杭州市各区", fontsize=8)
    # plt.show()

    # ------------------聚合--------------------------------

    # 分组计算不同行政区，薪水的最小值、最大值和平均值
    # df = df.groupby('district')['salary'].agg(['min', 'max', 'mean'])

    # 修改列名
    # df = df.groupby('district').agg(最低工资=('salary', 'min'), 最高工资=('salary', 'max'), 平均工资=('salary', 'mean')).rename_axis(["行政区"])

    # 对不同岗位(positionName)进行分组，并统计其薪水(salary)中位数和得分(score)均值
    # df = df.groupby('positionName').agg({'salary': 'median', 'score': 'mean'})

    # 对不同行政区进行分组，并统计薪水的均值、中位数、方差，以及得分的均值
    # df = df.groupby('district').agg({'salary': ['mean', 'median', 'std'], 'score': 'mean'})

    # 自定义函数 在聚合计算时新增一列计算最大值与平均值的差值
    # def myfunc(x):
    #     return x.max() - x.mean()
    # df = df.groupby('district').agg(最低工资=('salary', 'min'), 最高工资=('salary', 'max'), 平均工资=('salary', 'mean'),
    #                                 最大值与均值差值=('salary', myfunc)).rename_axis(["行政区"])

    # print(df)


if __name__ == '__main__':
    test_group_agg()
