import json
import vk
import vk_api
import csv
import time
import tok
import requests


# def get_comm():
vk_session = vk_api.VkApi(token=tok.t)
count = 100
offset = 0
vk = vk_session.get_api()
posts = vk.wall.get(owner_id='-72687742', count=count)['items']
all_posts = []

while offset < 100:
    with open('volnc_comments.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('id', 'post_id', 'from_id', 'text'))
        for post in posts:
            comments = vk.wall.getComments(owner_id='-72687742', post_id=post['id'], count=1000)['items']
            all_comments = []
            while offset < 100:
                for comment in comments:
                    try:
                        a_pen.writerow((comment['id'], comment['post_id'], comment['from_id'], comment['text']))
                    except:
                        pass
                data2 = json.loads(json.dumps(comments))
                all_comments.extend(data2)
                offset += 100

    data = json.loads(json.dumps(posts))
    offset += 100
    all_posts.extend(data)
    time.sleep(1)

print(1)