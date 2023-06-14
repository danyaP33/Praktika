import json
import vk_api
import csv
import time
import tok
import requests

vk_session = vk_api.VkApi(token=tok.t)
count = 100
offset = 0
vk = vk_session.get_api()

with open('volnc_commentss.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('id', 'post_id', 'from_id', 'text'))

    while offset < 1000:
        posts = vk.wall.get(owner_id='-72687742', count=count, offset=offset)['items']

        for post in posts:
            comments = vk.wall.getComments(owner_id='-72687742', post_id=post['id'], count=count)['items']
            for comment in comments:
                writer.writerow((comment['id'], comment['post_id'], comment['from_id'], comment['text']))

        offset += count
        time.sleep(1)

print(1)