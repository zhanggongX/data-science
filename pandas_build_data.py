import pandas as pd
import json
from glom import glom


def series_test():
    a = [1, 2, 3]
    pds_a = pd.Series(a)
    print(pds_a)
    print(pds_a[1])

    print("----------------")
    b = ["google", "tiktok", "alibaba"]
    pds_b = pd.Series(b, index={1, 2, 3})
    print(pds_b)
    print(pds_b[2])

    print("----------------")
    c = {1: "google", 2: "tiktok", 3: "alibaba"}
    pds_c = pd.Series(c)
    print(pds_c)
    # 只使用前两个
    pds_d = pd.Series(c, index=[1, 2])
    print(pds_d)
    pds_f = pd.Series(c, index=[1, 2], name="web_site")
    print(pds_f)


def data_frame_test():
    # pandas.DataFrame(data, index, columns, dtype, copy)
    a = [["google", 10], ["tiktok", 12], ["alibaba", 13]]
    df_a = pd.DataFrame(a, columns=["site", "age"])
    df_a.astype({"age": "float"})
    print(df_a)

    print("----------------")
    b = {"site": ["google", "tiktok", "alibaba"], "age": [10, 11, 12]}
    df_b = pd.DataFrame(b)
    # df_b.set_index("site", inplace=True)
    print(df_b)
    # print(df_b["tiktok"])


def data_frame_query():
    a = [["google", 10], ["tiktok", 12], ["alibaba", 13]]
    df_a = pd.DataFrame(a, columns=["site", "age"])
    print(df_a.loc[0])
    print(df_a.loc[1])
    print(df_a.loc[[1, 2]])


def data_frame_file():
    df_a = pd.read_csv("/Users/zhanggong/Downloads/test1.csv")
    print(df_a.head(2))
    # df_col = ["test1", "test2"]
    df_a["备注"] = ["test1", "test2", "test3", "test4"]
    print(df_a.info())
    # df_a.to_csv("/Users/zhanggong/Downloads/test2.csv")


def data_frame_json():
    df_json = pd.read_json("pandas_test.json");
    print(df_json)

    # URL = "https://github.com/***/pandas_test1.json"
    # df_json_1 = pd.read_json(URL)
    # print(df_json_1)
    df_json_1 = pd.read_json('pandas_test1.json')
    print(df_json_1)

    print("----------------")
    # 加载 json 数据 ps : need import json
    with open('pandas_test1.json', 'r') as f:
        data = json.loads(f.read())
        print(data)
    df_json_2 = pd.json_normalize(data, record_path=['students'])
    print(df_json_2)
    df_json_3 = pd.json_normalize(data, record_path=['students'], meta=['school_name', 'class'])
    print(df_json_3)

    print("----------------")
    with open('pandas_test2.json', 'r') as f:
        data = json.loads(f.read())
        print(data)
    df_json_4 = pd.json_normalize(data, record_path=['students'],
                                  meta=['class', ['info', 'president'], ['info', 'contacts', 'tel']])
    print(df_json_4)

    print("----------------")
    df_json_5 = pd.read_json('pandas_test3.json')
    df_json_6 = df_json_5['students'].apply(lambda row: glom(row, 'grade.math'))
    print(df_json_6)


if __name__ == "__main__":
    # series_test()
    # data_frame_test()
    # data_frame_query()
    # data_frame_file()
    data_frame_json()
