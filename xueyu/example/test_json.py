import json

if __name__ == '__main__':
    f = open('../../data/某基金数据.json', 'r')
    w = f.readline()

    json_dict = json.loads(w)
    print(json_dict)

    json_str = json.dumps(json_dict)
    print(json_str)