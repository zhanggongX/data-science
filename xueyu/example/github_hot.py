import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

def request_url(url):
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def hot_github(keyword):
    url = 'https://github.com/trending/{0}'.format(keyword)
    main_url = 'https://github.com{0}'

    html = request_url(url)
    soup = BeautifulSoup(html, 'lxml')

    articles = soup.findAll(class_='Box-row')

    hot_projects = []
    for article in articles:
        # 链接
        link = article.find('h2').find('a').get('href')
        link = main_url.format(link)
        # 说明
        content = article.find('p').string
        if content is not None:
            content = content.strip()
        # 关注
        stars = article.find_all('div')[2].find('a').text
        if stars is not None:
            stars = stars.strip()

        hot_projects.append([link, content, stars])


    # print(hot_projects)
    pd.DataFrame(hot_projects, columns=['链接', '说明', '关注数']).to_csv('./github_hot.csv', index=False)

if __name__ == '__main__':
    # keyword = input('请输入查找的热门语言:')
    hot_github('java')