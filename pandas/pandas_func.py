import pandas as pd
import pymysql as mysql
from sqlalchemy import create_engine


def pandas_read():
    df = pd.read_csv('test.csv')
    print(df)
    # engine = create_engine('jdbc:mysql://localhost:3306')
    # engine = create_engine('mysql+mysqldb://root:mysql@localhost:3306/blog')
    # df_sql = pd.read_sql("select * from article", engine)
    # pd.read_sql(sql, engine)
    con = mysql.connect(host='localhost', port=3306, user='root', password='mysql', charset='utf8', database='blog')
    df_sql = pd.read_sql("select * from article", con)
    print(df_sql)
    df_sql.info()

    print(df_sql.head(1))
    print(df_sql.tail(1))

    print(df_sql.describe())
    print(df_sql.shape)

    # 读取 JSON 数据
    df = pd.read_json('data.json')

    # 删除缺失值
    df = df.dropna()

    # 用指定的值填充缺失值
    df = df.fillna({'age': 0, 'score': 0})

    # 重命名列名
    df = df.rename(columns={'name': '姓名', 'age': '年龄', 'gender': '性别', 'score': '成绩'})

    # 按成绩排序
    df = df.sort_values(by='成绩', ascending=False)

    # 按性别分组并计算平均年龄和成绩
    grouped = df.groupby('性别').agg({'年龄': 'mean', '成绩': 'mean'})

    # 选择成绩大于等于90的行，并只保留姓名和成绩两列
    df = df.loc[df['成绩'] >= 90, ['姓名', '成绩']]

    # 计算每列的基本统计信息
    stats = df.describe()

    # 计算每列的平均值
    mean = df.mean()

    # 计算每列的中位数
    median = df.median()

    # 计算每列的众数
    mode = df.mode()

    # 计算每列非缺失值的数量
    count = df.count()


if __name__ == '__main__':
    pandas_read()
