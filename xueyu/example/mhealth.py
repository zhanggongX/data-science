import requests

from xueyu.example.parse_header import ParseHeader


def get_header_info() -> list:
    lines = []

    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return lines


if __name__ == "__main__":
    # 设置请求头
    base_url = 'https://mp.mhealth100.com'
    path = '/gateway/registration/appointment/schedule/find?branchCode=100238001&deptId=1240306&deptName=%25E7%2594%259F%25E6%25AE%2596%25E5%258C%25BB%25E5%25AD%25A6%25E4%25B8%25AD%25E5%25BF%2583%25E5%25A6%2587%25E7%25A7%2591&deptType=&startDate=2024-09-12&endDate=2024-09-12&ajaxConfig=true'

    lines = get_header_info()
    # headers = ParseHeader.do_parse(lines)
    cookies = ParseHeader.do_parse_cookie(lines)

    # r = requests.get(base_url + path, headers=headers, cookies=cookies)
    r = requests.get(base_url + path, cookies=cookies)
    print('请求结果：')
    print(r.text)
