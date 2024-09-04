import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
import seaborn as sns

'''
数据探索和描述性统计分析
'''


def test_statistics_data():
    top_university_file_path = '../../../data/university_rank_2024.xlsx'
    df = pd.read_excel(top_university_file_path)

    # 查看指定行
    # print(df.head(10))

    # 查看数据量
    # print(df.size)

    # 升序
    # print(df.sort_values('总分', ascending=True).head(20))

    # 指定列排序
    # print(df.nlargest(10, '高端人才得分'))
    # print(df.sort_values('高端人才得分', ascending=False).head(10))

    # 查看各项得分最高的学校名称
    # print(df.iloc[:, 3:].idxmax())

    # 计算总分列的均值
    # print(df.总分.mean())

    # 计算总分列的中位数
    # print(df.总分.median())

    # 计算总分列的众数
    # print(df.总分.mode())

    # 计算 总分、高端人才得分、办学层次得分的最大最小值、中位数、均值
    # print(df.agg({
    #     "总分": ["min", "max", "median", "mean"],
    #     "高端人才得分": ["min", "max", "median", "mean"],
    #     "办学层次得分":["min", "max", "median", "mean"]}))

    # 查看数值型数据的统计信息（均值、分位数等），并保留两位小数
    # df.describe().round(2).T

    # 计算各省市总分均值
    # print(df.groupby("省市")['总分'].mean())

    # 也就是相关系数矩阵，也就是每两列之间的相关性系数
    # print(df.corr())

    # 热力图
    ### 方法一
    # df.corr().style.background_gradient(cmap='coolwarm').set_precision(2)
    ### 方法二
    # 借助 `matplotlib` 和 `seaborn`
    # import seaborn as sns
    # import matplotlib.pyplot as plt
    #
    # plt.figure(figsize=(9, 6), dpi=100)
    # sns.set(font='Songti SC')
    # sns.heatmap(df.corr().round(2), annot=True, cmap='RdBu')
    # plt.show()

    # 计算各省市出现的次数
    # print(df.省市.value_counts())

    # 结合 pyecharts 将各省市高校上榜数量进行地图可视化
    # list1 = list(pd.DataFrame(df.省市.value_counts()).index)
    # list2 = list(pd.DataFrame(df.省市.value_counts()))
    # c = (
    #     Map()
    #     .add('', [list(z) for z in zip(list1, list2)], "china", is_map_symbol_show=False)
    #     .set_global_opts(
    #         title_opts=opts.TitleOpts(title="排名前100高校各省市占比"),
    #         visualmap_opts=opts.VisualMapOpts(max_=20),
    #     )
    # )
    # # 展示在notebook中
    # c.render_notebook()

    # 绘制总分的直方图、密度估计图
    # plt.figure(figsize=(9, 6), dpi=100)
    # sns.set(font='Songti SC')
    # sns.distplot(df['总分'])
    # plt.show()


if __name__ == '__main__':
    test_statistics_data()
