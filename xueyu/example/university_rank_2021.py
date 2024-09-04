import re
import requests
import pandas as pd

'''
中国大学排名2021
'''


# def get_info()

def get_page(url):
    js_content = ''
    res = requests.get(url, timeout=200)
    if res.status_code == 200:
        res.encoding = 'utf-8'
        js_content = res.text
    else:
        return

    # print(js_content)

    dict_key_re = re.compile('\(function\((.*)\)\{', re.S)
    dict_key_content = re.findall(dict_key_re, js_content)
    dict_keys = dict_key_content[0].split(',')

    dict_value_re = re.compile('}\((.*)\)\)\);$')
    dict_value_content = re.findall(dict_value_re, js_content)

    # 正则表达式
    pattern = r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)'
    # 使用正则表达式进行分割
    dict_vals = re.split(pattern, dict_value_content[0])
    real_dict_vals = []
    for dict_val in dict_vals:
        dict_val = dict_val.strip()
        if dict_val.startswith('"') or dict_val.endswith('"'):
            dict_val = dict_val.replace('"', '')
        real_dict_vals.append(dict_val)

    char_dict = dict(zip(dict_keys, real_dict_vals))

    all_universities = re.findall('\{(univUp.*?\})\}', js_content, re.S)
    # univUp:"tsinghua-university",univLogo:"logo\u002F27532357.png",univNameCn:"清华大学",univNameEn:"Tsinghua University",inbound:b,liked:b,univLikeCount:cq,univTags:[i,l,j],univNameRemark:a,univCategory:f,province:q,score:969.2,ranking:dX,rankChange:c,rankOverall:dX,indData:{"159":Z,"160":"74.3","161":"39.4","162":"48.7","163":"343.0","164":dY,"165":Z,"166":"90.8","167":"129.1","168":"80.1"}
    per_universities_re = re.compile(
        '.*univNameCn:"(.*)",univNameEn:(.*?),.*univTags:(.*],?),.*univCategory:(.*),province:(.*),score:(.*),ranking:(.*),rankChange.*indData:{"159":(.*),"160":(.*),"161":(.*),"162":(.*),"163":(.*),"164":(.*),"165":(.*),"166":(.*),"167":(.*),"168":(.*)}',
        re.S)

    res = []
    for per_university in all_universities:
        university_contents = re.findall(per_universities_re, per_university)
        university_content = university_contents[0]

        content = []
        for key in university_content:
            key = key.strip()
            if key.startswith('"') or key.endswith('"'):
                key = key.replace('"', '')

            if key in char_dict:
                key = char_dict[key]
            elif ']' in key:
                key_str = []
                key = key.replace('[', '').replace(']', '').split(',')
                if 'i' in key or 'l' in key or 'j' in key:
                    for kk in key:
                        key_str.append(char_dict[kk])
                key = ','.join(key_str)
            content.append(key)

        res.append(content)
    return res


if __name__ == '__main__':
    # 2021
    path = 'https://www.shanghairanking.cn/_nuxt/static/1723540750/rankings/bcur/202111/payload.js'
    all_datas = get_page(path)

    cols = ['学校名称', '学校英语名称', '学校标签', '学校分类', '省市', '总分', '排名', '办学层次得分',
            '学科水平得分', '办学资源', '师资规模与结构得分', '人才培养得分', '科学研究得分', '社会服务得分',
            '高端人才得分',
            '重大项目与成果得分', '国际竞争力得分']
    df = pd.DataFrame(all_datas, columns=cols)
    rank_col = df.pop('排名')
    df.insert(0, '排名', rank_col)
    df.set_index('排名', inplace=True)
    df.to_excel('university_rank_2021.xlsx')
