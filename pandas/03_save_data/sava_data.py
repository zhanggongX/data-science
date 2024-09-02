from operator import index

import pandas as pd

'''
pandas 读取 json 数据
'''


def test_save_data():
    json_file_path = '../../data/某基金数据.json'

    df = pd.read_json(json_file_path)

    # 将数据保存为 csv 格式
    # df.to_csv('out.csv', encoding='utf-8_sig')

    # 只保存特定的列
    # df.to_csv("out.csv", encoding='utf_8_sig', columns=['净值日期', '单位净值'])

    # 取消索引
    # df.to_csv("out.csv", encoding='utf_8_sig', index=False)

    # 在保存的同时，将缺失值标记为'数据缺失'
    # df.to_csv("out.csv", encoding='utf_8_sig', index=False, na_rep='数据缺失')

    # 将上面的数据保存至 zip 文件，解压后出现 out.csv
    # compression_opts = dict(method='zip', archive_name='out.csv')
    # df.to_csv('out.zip', index=False, compression=compression_opts)

    # 将数据保存为 xlsx 格式
    # df.to_excel("test.xlsx")

    # 将数据保存为 json 格式
    # df.to_json("out.json")

    # 将数据转换为 markdown 形式表格，这样可以直接复制进 .md 文件中使用
    # md_text = df.head().to_markdown(index = False)
    # 打印 md_text
    # print(md_text)

    # 保存成 html 文件
    df.to_html("out.html", col_space=100, index=False, justify='center', border=1)


if __name__ == '__main__':
    test_save_data()
