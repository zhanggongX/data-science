import requests
import pandas as pd
from bs4 import BeautifulSoup
from six import moves


def request_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.146 Safari/537.36',
    }

    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def save_to_excel(soup):
    list = soup.find(class_='grid_view').find_all('li')
    movies = []
    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if item.find(class_='inq') is not None:
            item_intr = item.find(class_='inq').string
        else:
            item_intr = 'NOT AVAILABLE'

        movies.append([item_index, item_name, item_img, item_score, item_author, item_intr])
        # print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)
    return movies



def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    html = request_url(url)
    soup = BeautifulSoup(html, 'lxml')
    movies = save_to_excel(soup)
    return movies

if __name__ == "__main__":
    all_movies = []
    for i in range(0, 10):
        moves = main(i)
        all_movies.extend(moves)
    pd.DataFrame(all_movies, columns=['index', 'name', 'img', 'score', 'author', 'intr']).to_excel('douban.xlsx', index=False)
