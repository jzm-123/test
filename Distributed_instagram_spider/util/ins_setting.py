import pymongo
import redis
import json
import os
from urllib.request import urlretrieve


def getValue(key):
    homedir = os.path.dirname(os.path.realpath(__file__))
    filepath = homedir + "/Config/Config.json"
    f = open(filepath, encoding='utf-8')
    setting = json.load(f)
    value = setting[key]
    return value


HOST = getValue('mongo_url')


# Get the cookies you need to log in
def get_cookies(HOST):
    conn = pymongo.MongoClient(HOST, 27017)
    db = conn['instagram']
    instagram_cookie_collection = db['instagram_account']
    cookies = []
    for instagram_cookie in instagram_cookie_collection.find():
        if instagram_cookie['status'] == 1:
            cookies.append(instagram_cookie['cookie'])
    return cookies


# get the proxyEnable
def get_proxyEnable(HOST, cookies):
    conn = pymongo.MongoClient(host=HOST, port=27017)
    db = conn['instagram']
    coll = db['instagram_account']
    for doc in coll.find():
        if doc['cookie'] == cookies:
            return doc['proxyEnable']


# get the proxy
def get_proxy(HOST, cookies):
    conn = pymongo.MongoClient(host=HOST, port=27017)
    db = conn['instagram']
    coll = db['instagram_account']
    for doc in coll.find():
        if doc['cookie'] == cookies:
            return doc['proxy']


# get the proxy_pass
def get_proxy_pass(HOST, cookies):
    conn = pymongo.MongoClient(host=HOST, port=27017)
    db = conn['instagram']
    coll = db['instagram_account']
    for doc in coll.find():
        if doc['cookie'] == cookies:
            return bytes(doc['proxy_pass'], encoding="utf-8")


# get the account from the mongo database
def get_account(cookies):
    cookie = cookies[0].decode('utf-8')
    cookieDict = {}
    items = cookie.split(";")
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        cookieDict[key] = value
    conn = pymongo.MongoClient(host=HOST, port=27017)
    db = conn['instagram']
    coll = db['instagram_account']
    for doc in coll.find():
        if doc['cookie']['sessionid'] == cookieDict['sessionid']:
            return doc['user']


# Determine if a post exists
# def isExistItemId(item_id, url):
#     host = url.split("/")[0]
#     db = int(url.split("/")[1])
#     r = redis.Redis(host=host, port=6379, db=db)
#     list_count = r.llen('twitter_tweets:items')
#     Flag = True
#     for index in range(list_count):
#         data = r.lindex('twitter_tweets:items', index)
#         postitem = json.loads(data)
#         if item_id == postitem['itemId']:
#             Flag = False
#             break
#         else:
#             Flag = True
#     return Flag


# Insert a task queue into the redis database
def InsertToRedis(name, value, url):
    host = url.split('/')[0]
    db = int(url.split('/')[1])
    r = redis.Redis(host=host, db=db, port='6379')
    r.lpush(name, value)


# Add a status task to the redis
def AddRedis(url, value):
    host = url.split('/')[0]
    db = int(url.split('/')[1])
    r = redis.Redis(host=host, db=db, port='6379')
    result = json.dumps(value)
    r.lpush("instagram_status", result)


# update the data from redis
def UpdateInfo(url, spider_name, key, value, string):
    host = url.split('/')[0]
    db = int(url.split('/')[1])
    r = redis.Redis(host=host, port=6379, db=db)
    list_count = r.llen("instagram_status")
    for index in range(list_count):
        json_str = r.lindex("instagram_status", index)
        data = json.loads(json_str)
        if data['spider_name'] == spider_name and data[key] == value:
            str1 = json.dumps(string)
            r.lset("instagram_status", index, str1)


# get the status of userinfo
def getStatus(url, spider_name, key, value):
    host = url.split('/')[0]
    db = int(url.split('/')[1])
    r = redis.Redis(host=host, db=db, port=6379)
    list_count = r.llen("instagram_status")
    for index in range(list_count):
        json_str = r.lindex("instagram_status", index)
        data = json.loads(json_str)
        if data['spider_name'] == spider_name and data[key] == value:
            return data['status']


# update the status of account
def UpdateCookieStatus(account, url, status, cookie_ban_timestamp):
    host = url.split('/')[0]
    conn = pymongo.MongoClient(host, 27017)
    db = conn['instagram']
    colls = db['instagram_account']
    colls.update({'user': account}, {'$set': {'status': status, 'cookie_ban_timestamp': cookie_ban_timestamp}})

# Determine whether it exits value
# def determine_screen_name(screen_name, url):
#     host = url.split('/')[0]
#     db = int(url.split('/')[1])
#     r = redis.Redis(host=host, port=6379, db=db)
#     list_count = r.llen('twitter_follow:items')
#     flag = False
#     for index in range(list_count):
#         json_str = r.lindex('twitter_follow:items', index)
#         data = json.loads(json_str)
#         if data['fan_screen_name'] == screen_name:
#             flag = True
#             break
#     return flag


# Get the hop of friends
def get_hop(friends_screen_name, url):
    host = url.split('/')[0]
    db = int(url.split('/')[1])
    r = redis.Redis(host=host, port=6379, db=db)
    list_count = r.llen('instagram_follow:items')
    for index in range(list_count):
        json_str = r.lindex('instagram_follow:items', index)
        data = json.loads(json_str)
        if data['fan_screen_name'] == friends_screen_name:
            return data['followHop']

# download the image
def urllib_download(image_url, image_path, image_name):
    os.makedirs(image_path, exist_ok=True)
    urlretrieve(image_url, image_name)


# write the status
def writeToJson(data):
    scrpath = os.path.abspath(os.path.join(os.getcwd(), "../../.."))
    filepath = scrpath + "/image_status"
    jsonfilepath = scrpath + "/image_status/image.json"
    if not os.path.exists(jsonfilepath):
        os.makedirs(filepath)
        new = []
        new.append(data)
        with open(jsonfilepath, "w") as f:
            jsonstr = json.dumps(new)
            f.write(jsonstr)
    else:
        f = open(jsonfilepath)
        pictures = []
        if f is None:
            settings = []
        else:
            settings = json.load(f)
            pictures = settings
        for i in range(0, len(settings)):
            if data['fileName'] == settings[i]['fileName'] and data['jobId'] == settings[i]['jobId']:
                pictures[i]['status'] = data['status']
                break
            if i == len(settings) - 1:
                pictures.append(data)
        with open(jsonfilepath, "w") as f:
            jsonstr = json.dumps(pictures)
            f.write(jsonstr)


# get the lma of account
def get_lma(account):
    conn = pymongo.MongoClient(host=HOST, port=27017)
    db = conn['instagram']
    colls = db['instagram_account']
    print('user:', account)
    data = colls.find_one({"user": account})
    # print('account:',data)
    return data['lma']


# get user_id
# def get_user_id(url, screen_name):
#     host = url.split('/')[0]
#     db = int(url.split('/')[1])
#     r = redis.Redis(host=host, db=db, port=6379)
#     list_count = r.llen("userinfo:items")
#     for index in range(list_count):
#         json_str = r.lindex("userinfo:items", index)
#         # print('json:',str(json_str,encoding='utf-8'))
#         # print('json:',json_str.decode("utf-8"))
#         data = json.loads(json_str.decode("utf-8"))
#         # print('data:',type(data))
#         if data['screen_name'] == screen_name:
#             return data["user_id"]


# Distributed instagram's user_agents
USER_AGENTS = ['Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0']

# 以下hash值通过js生成
query_hash = "c76146de99bb02f6415203be841dd25a"  # 粉丝查询hash值
query_hash2 = "d04b0a864b4b54837c0d870b0e77e076"  # 关注查询hash值
query_hash3 = "f2405b236d85e8296cf30347c9f08c2a"  # 帖子查询hash值
query_hash4 = "97b41c52301f77ce508f55e66d17620e"  # 评论查询hash值
query_hash5 = "51fdd02b67508306ad4484ff574a0b62"  # 子评论查询hash值