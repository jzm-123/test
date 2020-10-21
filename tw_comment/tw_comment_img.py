import json
import re
import time
with open('tw_img.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
def str2timestamp(time_str):
    month = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    time_list = time_str.split(" ")
    for order, mon in enumerate(month):
        if time_list[1] == mon:
            m = str(order) if len(str(order)) == 2 else "0" + str(order)
            break
    t = "-".join([time_list[5], m, time_list[2]]) + " " + time_list[3]
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(timeArray)) + 8 * 3600
    return t, time_stamp
reply_tweets =data['globalObjects']['tweets']
imgs = []
for comments_id, item in reply_tweets.items():
    cid_str = item['id_str']
    # print(cid_str)
    if 'extended_entities' in item.keys():
        if "media" in item['extended_entities'].keys():
            media=item["extended_entities"]["media"]
            for md in media:
                imgs.append(md["media_url"])
    ccreated_at, ccreated_at_int = str2timestamp(item['created_at'])
    # print(ccreated_at_int)
print(imgs)
#