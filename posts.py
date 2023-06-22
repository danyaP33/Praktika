import csv
import time
import requests
import tok

def get_posts():
    token = tok.t
    version = 5.131
    owner_id = '-33086750'
    count = 100
    offset = 0
    all_posts = []

    while offset < 65000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'owner_id': owner_id,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(1)

    return all_posts


def file_writer_posts(data):
    with open('cherepistina_posts.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('id', 'date', 'likes', 'reposts', 'comments', 'views', 'text'))
        for post in data:
            try:
                a_pen.writerow((post['id'], post['date'], post['likes']['count'], post['reposts']['count'],
                                post['comments']['count'], post['views']['count'], post['text']))
            except:
                pass


all_posts = get_posts()

file_writer_posts(all_posts)

print(1)