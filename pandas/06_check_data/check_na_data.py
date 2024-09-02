import pandas as pd

'''
pandas 检查数据
'''


def test_check_data():
    douban_top_250_path = '../../data/TOP250.xlsx'
    df = pd.read_excel(douban_top_250_path)

    # 检查全部缺失值
    # print(df.isna().sum().sum())

    # 检查每列缺失值
    # print(df.isnull().sum())

    # 定位缺失值
    # print(df[df.isnull().T.any() == True])

    # pip install jinja2
    # 缺失值进行高亮进一步查看
    # df = df[df.isnull().T.any() == True]
    # df.style.highlight_null(color='skyblue').set_table_attributes('style="font-size: 10px"').to_html('out.html')

    # 将缺失值出现的行全部删掉
    # df = df.dropna()

    # 将全部缺失值替换为 *
    # df = df.fillna('*')

    # 现在将评分列的缺失值，替换为上一个电影的评分
    # df['评分'] = df['评分'].fillna(axis=0, method='ffill')

    # 将评价人数列的缺失值，用整列的均值进行填充
    # df['评价人数'] = df['评价人数'].fillna(df['评价人数'].mean())

    # 将评价人数列的缺失值，用上下数字的均值进行填充
    # df['评价人数'] = df['评价人数'].fillna(df['评价人数'].interpolate())

    # 填充 “语言” 列的缺失值，要求根据 “国家/地区” 列的值进行填充
    # df['语言'] = df.groupby('国家/地区').语言.bfill()
    print(df)



if __name__ == '__main__':
    test_check_data()
