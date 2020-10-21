import os
import re
import sys
import json
import time
import random
import requests
from hashlib import md5
from pyquery import PyQuery as pq
from urllib import parse, response

url_base = 'https://www.instagram.com/'
url = 'https://www.instagram.com/ibramxk/'
base_url = 'https://www.instagram.com/graphql/query/?query_hash={0}&variables={1}'
url_test = 'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%20%224055534935%22%2C%20%22first%22%3A%2050%2C%20%22include_reel%22%3A%20%22false%22%7D'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'cookie': 'ig_did=DACDB5EF-FF8C-4F9D-BDCE-44B155CC59D8; mid=X2CEVwALAAHrWiqGcqh8zo8SjI-1; rur=FRC; urlgen="{\"149.28.30.148\": 20473\054 \"13.88.218.237\": 8075\054 \"42.2.74.52\": 4760}:1kIu0i:vLYe-GAFt_lVir8A9Wiijm7tpVM"; csrftoken=CUJtYkFZPWsJneRiYgBOt2TFW8jh7bs1; ds_user_id=41685624894; sessionid=41685624894%3Aigp9ARRJLyuhaT%3A24'
}


def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print('请求网页源代码错误, 错误状态码：', response.status_code)
    except Exception as e:
        print(e)
        return None


def get_json(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print('请求网页json错误, 错误状态码：', response.status_code)
    except Exception as e:
        print(e)
        time.sleep(60 + float(random.randint(1, 4000))/100)
        return get_json(url)


def get_content(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.content
        else:
            print('请求照片二进制流错误, 错误状态码：', response.status_code)
    except Exception as e:
        print(e)
        return None


def get_urls(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print('请求错误状态码：', response.status_code)
    except Exception as e:
        print(e)
        return None
url1='https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%20%225951385086%22%2C%20%22first%22%3A%2050%7D'
post='https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%20%225951385086%22%2C%20%22first%22%3A%2050%7D'
son_comment_num='https://www.instagram.com/graphql/query/?query_hash=7da1940721d75328361d772d102202a9&variables=%7B%22shortcode%22%3A%22CFbBrXbjWJl%22%2C%22child_comment_count%22%3A3%2C%22fetch_comment_count%22%3A40%2C%22parent_comment_count%22%3A24%2C%22has_threaded_comments%22%3Atrue%7D'
html = get_urls(son_comment_num)

# Cookie = response.request.headers.getlist('Cookie')
# print(Cookie)
j=json.loads(html)
list = j["data"]["shortcode_media"]["edge_media_to_parent_comment"]["edges"]
for i in list:
    son_comment_num = i["node"]["edge_threaded_comments"]["count"]
    print(son_comment_num)
# list = t["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
# user_id = list[0]["node"]["owner"]["id"]
# for i in list:
#     node = i["node"]
#     r = requests.get(node["display_url"], timeout=2)
#     print(r.content)
    # node = i["node"]  # 一个帖子结点
    # shortcode = node["shortcode"]
    # post_id = node["id"]
    # url = node["display_url"]
    # content = node["edge_media_to_caption"]["edges"][0]["node"]["text"]
    # time = node["taken_at_timestamp"]
    # likes = node["edge_media_preview_like"]["count"]
    # comment_num = node["edge_media_to_comment"]["count"]
    # user_id = user_id
    # shortcode = shortcode
    # is_video = node["is_video"]
    # print(post_id)
    # print(content)
    # print(time)
    # print(comment_num)
    # print(user_id)
    # print(is_video)
# p1 = re.compile(r'window._sharedData = (.*?);</script>', re.MULTILINE)
# j1 = re.findall(p1, html)[0]
# l1 = json.loads(j1)  # l1为sharedData中的json格式数据
# userinfo = l1["entry_data"]["ProfilePage"][0]["graphql"]["user"]
# urls = []
# doc = pq(html)
# items = doc('script[type="text/javascript"]').items()
# query_hash = '97b41c52301f77ce508f55e66d17620e'
# j = json.loads(html)
# list = j["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
# for i in list:
#     node = i["node"]  # 一个帖子结点
#     shortcode = node["shortcode"]
# for item in items:
#     if item.text().strip().startswith('window._sharedData'):
#         js_data = json.loads(item.text()[21:-1], encoding='utf-8')
#         userinfo = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
        # list = js_data["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
        # user_id = list[0]["node"]["owner"]["id"]
#         for i in list:
#             node = i["node"]  # 一个帖子结点
#             shortcode = node["shortcode"]
# print(userinfo["id"])
# print(userinfo["username"])
# print(userinfo["biography"])
        # print(userinfo["edge_owner_to_timeline_media"]["count"])
        # print(userinfo["edge_followed_by"]["count"])
        # print(userinfo["edge_follow"]["count"])
        # print(userinfo["is_verified"])
        # print(userinfo["external_url"])
    # vars = {"shortcode": shortcode, "first": 50}
    # text = json.dumps(vars)
    # url1 = base_url.format(query_hash, parse.quote(text))
    #     print(userinfo)