import json

import pandas as pd


def direct_analyze():
    df = pd.read_excel('data_1726297183.xlsx',
                       dtype={'direction_name': str, 'topic': str, 'rank_info': str, 'key_info': str,
                              'level_info': str})

    all_datas = []

    for i in range(len(df)):
        # 处理每一行
        row = df.loc[i]
        # 每一行的结果
        row_result = {}

        direction_name = row['direction_name']
        # 原值记录
        row_result['direction_name'] = direction_name

        # 原值记录
        topic = row['topic']
        row_result['topic'] = topic

        # 原值记录
        rank_info = row['rank_info']
        row_result['rank_info'] = rank_info

        try:
            # rank_info 转 json，由于结果可能为空，所以捕获异常
            rank_info_json = json.loads(rank_info)
        except Exception:
            # 该行加入总记录
            all_datas.append(row_result)
            continue

        # 记录分析结果
        analyze_result = {}

        key_info = row['key_info']
        row_result['key_info'] = key_info
        # key_info 转 json
        key_info_json = json.loads(key_info)

        level_info = row['level_info']
        row_result['level_info'] = level_info
        # level_info 转 json
        level_info_json = json.loads(level_info)

        for item in rank_info_json:
            # k = item
            # v = rank_info_json[item]

            # 保存原纪录
            item_val = rank_info_json[item]
            analyze_result[item] = item_val

            # 后边存的值的字符串。
            item_val_str = str(item_val)

            if item_val_str in key_info_json:
                analyze_result['key_info_' + item] = key_info_json[str(item_val)]
            if item_val_str in level_info_json:
                analyze_result['level_info_' + item] = level_info_json[str(item_val)]

        # 最终分析结果，保存入 all_datas
        row_result['analyze_result'] = json.dumps(analyze_result, ensure_ascii=False)
        all_datas.append(row_result)

    # 保存 excel
    df = pd.DataFrame(all_datas)
    df.to_excel('result1.xlsx')


if __name__ == '__main__':
    direct_analyze()
