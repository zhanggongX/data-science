import pandas as pd

'''
pandas 读取 json 数据
'''

def test_read_json():
    json_file_path = '../../data/某基金数据.json'

    df = pd.read_json(json_file_path)
    print(df)

if __name__ == '__main__':
    test_read_json()