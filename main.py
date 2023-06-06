import csv
import datetime
import time
import vk
import vk_api
import requests
import tok


def get_comments():
    t = tok.t
    version = 5.131
    owner_id = '-72687742'
    post_id = '8272'
    count = 100
    offset = 0
    sort = 'asc'
    all_comments = []

    while offset < 100:
        response = requests.get('https://api.vk.com/method/wall.getComments',
                                params={
                                    'access_token': t,
                                    'v': version,
                                    'owner_id': owner_id,
                                    'post_id': post_id,
                                    'count': count,
                                    'offset': offset,
                                    'sort': sort
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_comments.extend(data)
        time.sleep(1)

    return all_comments


def file_writer_comments(data):
    with open('volnc_comments.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('id', 'post_id', 'date', 'from_id', 'text'))
        for comments in data:
            try:
                a_pen.writerow((comments['id'], comments['post_id'], comments['date'], comments['from_id'], comments['text']))
            except:
                pass

all_comments = get_comments()

file_writer_comments(all_comments)


def get_posts():
    token = '02f8dab702f8dab702f8dab7be01ecf55c002f802f8dab76687df60128d177b70813cb1'
    version = 5.131
    owner_id = '-72687742'
    count = 100
    offset = 0
    all_posts = []

    while offset < 100:
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
    with open('volnc_posts.csv', 'w', encoding='utf-8') as file:
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
