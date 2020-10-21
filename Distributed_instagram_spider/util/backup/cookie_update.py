import  pymongo
import random

HOST = "127.0.0.1"

#取得登录所需要的cookies
def get_ins_cookies():
    conn = pymongo.MongoClient(HOST, 27017)
    db = conn['ins']
    twitter_cookie_collection = db['cookie_update']
    cookies = []

    for twitter_cookie in twitter_cookie_collection.find():
        cookies.append(twitter_cookie['cookie'])
    return cookies

#将随机表中的cookie所对应的account返回出来
def get_cookie_account(cookie):
    conn = pymongo.MongoClient(HOST, 27017)
    db = conn['ins']
    twitter_cookie_collection = db['cookie_update']

    for twitter_cookie in twitter_cookie_collection.find():
        if twitter_cookie['cookie']== cookie:
            return twitter_cookie['account']

test = get_ins_cookies()
test_cookie = random.choice(test)
print('account',get_cookie_account(test_cookie))