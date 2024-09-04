import requests

if __name__ == "__main__":
    print(1)

    # 简单请求
    # ret = requests.get('https://api.github.com/events')
    # r = requests.post('https://httpbin.org/post', data={'key': 'value'})
    # r = requests.put('https://httpbin.org/put', data={'key': 'value'})
    # r = requests.delete('https://httpbin.org/delete')
    # r = requests.head('https://httpbin.org/get')
    # r = requests.options('https://httpbin.org/get')
    # r = requests.get('https://github.com/', timeout=0.001)

    # 带参请求
    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.get('https://httpbin.org/get', params=payload)

    # 设置请求头
    # url = 'https://api.github.com/some/endpoint'
    # headers = {'user-agent': 'my-app/0.0.1'}
    # r = requests.get(url, headers=headers)

    # 一个键里面添加多个值
    # payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
    # r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
    # payload_dict = {'key1': ['value1', 'value2']}
    # r2 = requests.post('https://httpbin.org/post', data=payload_dict)
    # print(r1.text)
    # print(r1.text == r2.text)

    # json 作为参数
    # url = 'https://api.github.com/some/endpoint'
    # payload = {'some': 'data'}
    # r = requests.post(url, json=payload)

    # 上传文件
    # url = 'https://httpbin.org/post'
    # files = {'file': open('report.xls', 'rb')}
    # r = requests.post(url, files=files)

    # 获取 cookie
    # url = 'http://example.com/some/cookie/setting/url'
    # r = requests.get(url)
    # print(r.cookies['example_cookie_name'])

    # 发送 cookie
    # url = 'https://httpbin.org/cookies'
    # cookies = dict(cookies_are='working')
    # r = requests.get(url, cookies=cookies)

    # print(r.encoding)
    # print("----------------")
    # print(r.text)
    # print("----------------")
    # print(r.content)
    # print("----------------")
    # print(r.status_code)
    # print("----------------")
    # print(r.headers)
    # print("----------------")
    # print(r.json())
    # print("----------------")
    # # socket 流
    # print(r.raw)
    # print("----------------")
