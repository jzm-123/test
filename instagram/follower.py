import json
import re
with open('follower.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
list = data["data"]["user"]["edge_followed_by"]["edges"]
for i in list:
    id = i["node"]["id"]
    follower_name = i["node"]["username"]
    print(id)
    print(follower_name)