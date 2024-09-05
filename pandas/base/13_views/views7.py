import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
个性化显示，option、style
'''


def test_pd_option():
    path = '../../../data/某招聘网站数据.csv'
    df = pd.read_csv(path)

    # 由于数据维度较大，部分行列会被折叠，显示为 ... ，现在需要显示全部的列方便预览。
    # pd.set_option('display.max_columns', None)  # 显示全部列
    # pd.set_option('display.max_rows', None) # 显示全部行

    # 在预览时显示10列，7行
    # pd.set_option('display.max_columns', 10)
    # pd.set_option('display.max_rows', 7)
    # # 还原设置
    # pd.reset_option("max_rows")
    # pd.reset_option("max_columns")

    # 显示所有列，但是每列最多显示10个字符，多余的会变成...
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_colwidth', 10)

    # 设置小数点位数
    # pd.set_option('display.precision', 5)

    # 还原所有的设置
    # pd.reset_option("^display")

    # 忽略警告
    # pd.set_option("mode.chained_assignment", None)
    # 全局取消warning
    # import warnings
    # warnings.filterwarnings('ignore')

    # 若数值小于 20 则显示为0
    # pd.set_option('chop_threshold', 20)

    # 让dataframe中内容支持 Latex 显示
    # pd.set_option("display.html.use_mathjax", True)

    # 修改pandas默认绘图引擎为plotly
    # pd.set_option("plotting.backend", "plotly")

    # 还原所有 option 设置
    # pd.reset_option("all")

    print(df.head())


def test_pd_style():
    path = '../../../data/某招聘网站数据.csv'
    df = pd.read_csv(path)

    # 模拟隐藏索引
    # df = df.style.hide(axis='index').set_table_attributes('style="font-size: 20px"')

    # 将带有小数点的列精度调整为小数点后2位
    # df = df.style.format(precision=2).set_table_attributes('style="font-size: 10px"')

    # 标记缺失值
    # df = df.fillna("数据缺失")
    # df = df.style.set_table_attributes('style="font-size: 10px"')

    # 将缺失值高亮，颜色名skyblue
    # df = df.style.set_na_rep("数据缺失").highlight_null(null_color='skyblue').set_table_attributes(
    #     'style="font-size: 10px"')

    # 高亮数值列最小值
    # df = df.style.highlight_max().set_table_attributes('style="font-size: 10px"')

    # 同时高亮最大最小值
    # df = df.style.highlight_max(color='#F77802').highlight_min(color='#26BE49').set_table_attributes(
    #     'style="font-size: 10px"')

    # 指定区间高亮
    # (data
    # .style
    # .highlight_between(left=3000, right=10000, subset=['salary'])
    # .set_table_attributes('style="font-size: 10px"'))

    # 渐变显示数值列
    # cm = sns.light_palette("green", as_cmap=True)
    # (data
    #  .style
    #  .background_gradient(cmap=cm)
    #  .set_table_attributes('style="font-size: 10px"'))


    # 修改字体颜色
    # (data
    #  .style
    #  .set_properties(
    #     subset=['salary'], **{'color': 'red'})
    #  .set_table_attributes('style="font-size: 10px"'))

    # 修改背景颜色、对齐方式、字体大小
    # (data
    #  .style
    #  .set_properties(**{'background-color': '#F8F8FF', 'text-align': 'center', 'font-size': '13px'})
    #  .set_table_attributes('style="font-size: 10px"'))


    # 综合(链式)设置
    # (data
    #  .style
    #  .set_properties(**{'background-color': '#F8F8FF', 'text-align': 'center', 'font-size': '13px'})
    #  .set_properties(
    #     subset=['salary'], **{'color': 'red'})
    #  .set_table_attributes('style="font-size: 10px"'))


    # 导出样式
    # (data
    # .style
    # .set_properties(**{'background-color': '#F8F8FF', 'text-align': 'center', 'font-size': '13px'})
    # .set_properties(
    #     subset=['salary'], **{'color': 'red'})).to_excel('带有样式导出.xlsx')

    # 制作指定列条形图
    # (data
    # .style
    # .bar(subset=['salary'],color='skyblue')
    # .set_table_attributes('style="font-size: 10px"'))

    # 自定义样式
    # def my_style(val):
    #     color = 'red' if val > 30000 else 'black'
    #     return 'color: %s' % color
    # data.style.applymap(my_style, subset="salary").set_table_attributes('style="font-size: 10px"')

    # 格式化输出日期类型，将 createTime 列格式化输出为 xx年xx月xx日
    # data.style.format({"createTime": lambda t: t.strftime("%Y年%m月%d日")}).set_table_attributes(
    #     'style="font-size: 10px"')

    # 自定义格式化数据
    # (data
    #  .style
    #  .format("{0:,.2f}分", subset="matchScore")
    #  .format("{""}元", subset="salary")
    #  .set_table_attributes('style="font-size: 10px"'))

    df.to_html('out.html')

    # print(df)


if __name__ == '__main__':
    # test_pd_option()
    test_pd_style()
