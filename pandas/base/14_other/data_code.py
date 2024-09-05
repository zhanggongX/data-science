import pandas as pd
# from sklearn.preprocessing import Binarizer

def test_data_code():
    df = pd.DataFrame({
        "Sex": pd.Series(['Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female']),
        "Course Name": pd.Series(['Python', 'Java', 'C', 'Sql', 'Linux', 'Python', 'Python', 'Java', 'C', 'Php']),
        "Score": [95, 85, 75, 65, 55, 95, 75, 65, 55, 85]})

    print(df)

    # 数值型数据编码
    # 1. 使用自定义函数 + 循环遍历
    # df1 = df.copy()
    # def myfun(x):
    #     if x > 90:
    #         return 'A'
    #     elif x >= 80 and x < 90:
    #         return 'B'
    #     elif x >= 70 and x < 80:
    #         return 'C'
    #     elif x >= 60 and x < 70:
    #         return 'D'
    #     else:
    #         return 'E'
    #
    # df1['Score_Label'] = None
    # for i in range(len(df1)):
    #     df1.iloc[i, 3] = myfun(df1.iloc[i, 2])
    # print(df1)

    # 2 - 使用 map + 自定义函数
    # df2 = df.copy()
    # def mapfun(x):
    #     if x > 90:
    #         return 'A'
    #     elif x >= 80 and x < 90:
    #         return 'B'
    #     elif x >= 70 and x < 80:
    #         return 'C'
    #     elif x >= 60 and x < 70:
    #         return 'D'
    #     else:
    #         return 'E'
    #
    # df2['Score_Label'] = df2['Score'].map(mapfun)
    # print(df2)

    # 3 - 使用 apply + 匿名函数
    # df3 = df.copy()
    # df3['Score_Label'] = df3['Score'].apply(lambda x: 'A' if x > 90 else (
    #     'B' if 90 > x >= 80 else ('C' if 80 > x >= 70 else ('D' if 70 > x >= 60 else 'E'))))
    # print(df3)

    # 4 - 使用 cut
    # df4 = df.copy()
    # bins = [0, 59, 70, 80, 100]
    # df4['Score_Label'] = pd.cut(df4['Score'], bins)
    # print(df4)

    # 4 - 使用 cut, 也可以直接使用labels参数来修改对应组的名称
    # df4 = df.copy()
    # bins = [0, 59, 70, 80, 100]
    # df4['Score_Label_new'] = pd.cut(df4['Score'], bins, labels=[
    #     'low', 'middle', 'good', 'perfect'])
    # print(df4)

    # df5 = df.copy()
    # binerize = Binarizer(threshold=60)
    # trans = binerize.fit_transform(np.array(df1['Score']).reshape(-1, 1))
    # df5['Score_Label'] = trans

    # 6 - 使用 replace
    # df6 = df.copy()
    # df6['Sex_Label'] = df6['Sex'].replace(['Male', 'Female'], [0, 1])
    # print(df6)

    # 7 - 使用map
    # df7 = df.copy()
    # Map = {elem: index for index, elem in enumerate(set(df["Course Name"]))}
    # df7['Course Name_Label'] = df7['Course Name'].map(Map)
    # print(df7)

    # 8 - 使用astype
    # df8 = df.copy()
    # value = df8['Course Name'].astype('category')
    # df8['Course Name_Label'] = value.cat.codes
    # print(df8)

    # 9 - 使用 sklearn
    # df9 = df.copy()
    # le = LabelEncoder()
    # le.fit(df9['Sex'])
    # df9['Sex_Label'] = le.transform(df9['Sex'])
    # le.fit(df9['Course Name'])
    # df9['Course Name_Label'] = le.transform(df9['Course Name'])
    # print(df9)

    # 10 - 使用factorize
    # df10 = df.copy()
    # df10['Course Name_Label'] = pd.factorize(df10['Course Name'])[0]
    # print(df10)



if __name__ == '__main__':
    test_data_code()
