import pandas as pd

'''
测试数据创建
'''


def test_create_data():
    l = [1, 2, 3, 4, 5]
    df = pd.DataFrame(l, columns=['num'])

    # 嵌套列表转换
    l = [[1, 2, 3], [4, 5, 6]]
    df = pd.DataFrame(l, index=['id', 'num'])

    # 从字典创建
    data = {"one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
            "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"])}
    df = pd.DataFrame(data)

    # 指定索引顺序
    df = pd.DataFrame(data, index=["d", "b", "a"])

    # 指定列名
    df = pd.DataFrame(data, index=["d", "b", "a"], columns=["two", "three"])

    # 字典列表
    data = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
    df = pd.DataFrame(data)

    # 从集合创建
    data = ((1, 0, 0, 0,), (2, 3, 0, 0,), (4, 5, 6, 0,), (7, 8, 9, 10,))
    df = pd.DataFrame(data, columns=[1, 2, 3, 4], index=[1, 2, 3, 4])
    print(df)


if __name__ == '__main__':
    test_create_data()
