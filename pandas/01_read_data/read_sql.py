import pandas as pd
import pymysql

'''
pandas 读取 json 数据
'''


def test_read_sql():
    db = pymysql.connect(host='localhost', port=3306, user='test', password='111111', db='test')

    sql = "select * from table_name where id > 0"

    cursor = db.cursor()

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[4]
            print(id, name)
    except:
        print('Error: unable to fetch data')

    db.close()


if __name__ == '__main__':
    test_read_sql()
