import json
import re
with open('userinfo.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
p1 = re.compile(r'window._sharedData = (.*?);</script>', re.MULTILINE)
j1 = re.findall(p1, response.text)[0]
l1 = json.loads(j1)  # l1为sharedData中的json格式数据
userinfo = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
id=userinfo["id"]
username=userinfo["username"]
biography=userinfo["biography"]
posts_num=userinfo["edge_owner_to_timeline_media"]["count"]
follower_num=userinfo["edge_followed_by"]["count"]
following_num=userinfo["edge_follow"]["count"]
is_verified=userinfo["is_verified"]
external_url=userinfo["external_url"]
external_url_linkshimmed=userinfo["external_url_linkshimmed"]
is_business_account=userinfo["is_business_account"]
is_joined_recently=userinfo["is_joined_recently"]
profile_pic_url=userinfo["profile_pic_url"]
business_account=userinfo["business_account"]
print(id)

