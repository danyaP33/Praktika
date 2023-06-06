import json
import vk
import vk_api
import csv
import time
import tok


# def get_comm():
vk_session = vk_api.VkApi(token=tok.t)
count = 100
offset = 0
vk = vk_session.get_api()
posts = vk.wall.get(owner_id='-72687742', count=count)['items']
all_posts = []

while offset < 1000:
    with open('volnc_comments.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('id', 'post_id', 'from_id', 'text'))
        for comment in comments:
            try:
                a_pen.writerow((comments['id'], comments['post_id'], comments['from_id'],
                                comments['text']))
            except:
                pass
    for post in posts:
        comments = vk.wall.getComments(owner_id='-72687742', post_id=post['id'])['items']

data = response.json()['response']['items']
offset += 100
all_posts.extend(data)
time.sleep(1)