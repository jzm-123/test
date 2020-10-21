import json
import re
import requests
import sys
import pymongo
import os
import time
import datetime
import pytz

out_headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Host": "www.instagram.com",
               }


class Fetcher(object):

    def __init__(self):
        self.loginUrl = "https://www.instagram.com/accounts/login/ajax/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36" }

    def login_proxy(self, username, password, proxies):
        loginSession = requests.Session()
        loginSession.proxies = proxies
        try:
            # print('http requests ing ... ', self.loginUrl)
            test_url = "http://www.instagram.com/jaychou/"
            res = loginSession.get(
                test_url, verify=False, timeout=5, allow_redirects=True)
            # print('http requests done ... ', res.url)
        except Exception as e:
            print(e)
            return None

        mid = res.cookies["mid"]
        csrftoken = res.cookies["csrftoken"]
        rur = res.cookies["rur"]
        urlgen = res.cookies["urlgen"]
        cookie = "mid=" + mid + "; csrftoken=" + csrftoken + "; rur=" + rur + "; urlgen=" + urlgen
        self.headers.update({
            "x-csrftoken": csrftoken,
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded",
            "rigin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/login/?source=auth_switcher",
            "cookie": cookie
        })

        payload = {
            "username": username,
            "password": password,
            "queryParams": "{\"source\": \"auth_switcher\"}",
            "optIntoOneTap": "true"
        }

        # userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
        # headers = {'User-Agent': userAgent,
        #            'Accept-Encoding': 'gzip, deflate, br',
        #            'Accept-Language': 'zh-CN,zh;q=0.8',
        #            'X-Requested-With': 'XMLHttpRequest'}
        try:
            # print('http requests ing ... ', url)
            res = loginSession.post(
                self.loginUrl, verify=False, headers=self.headers, data=payload, timeout=5, allow_redirects=True)
            # print('http requests done ... ', res.url)
        except Exception as e:
            print(Exception('My NetERR', e))
            return None

        req_cookie = requests.utils.dict_from_cookiejar(loginSession.cookies)
        # print(res.status_code)
        # print(req_cookie)

        loginSession.close()
        return req_cookie

    def login(self, username, password):
        loginSession = requests.Session()
        try:
            # print('http requests ing ... ', self.loginUrl)
            test_url = "http://www.instagram.com/jaychou/"
            res = loginSession.get(
                test_url, verify=False, timeout=5, allow_redirects=True)
            # print('http requests done ... ', res.url)
        except Exception as e:
            print(e)
            return None
        mid = res.cookies["mid"]
        csrftoken = res.cookies["csrftoken"]
        rur = res.cookies["rur"]
        urlgen = res.cookies["urlgen"]
        cookie = "mid=" + mid + "; csrftoken=" + csrftoken + "; rur=" + rur + "; urlgen=" + urlgen
        self.headers.update({
            "x-csrftoken": csrftoken,
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded",
            "rigin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/login/?source=auth_switcher",
            "cookie": cookie
        })

        payload = {
            "username": username,
            "password": password,
            "queryParams": "{\"source\": \"auth_switcher\"}",
            "optIntoOneTap": "true"
        }

        # userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
        # headers = {'User-Agent': userAgent,
        #            'Accept-Encoding': 'gzip, deflate, br',
        #            'Accept-Language': 'zh-CN,zh;q=0.8',
        #            'X-Requested-With': 'XMLHttpRequest'}

        try:
            # print('http requests ing ... ', url)
            res = loginSession.post(self.loginUrl, verify=False, headers=self.headers, data=payload, timeout=5,
                                    allow_redirects=True)
            # print('http requests done ... ', res.url)
        except Exception as e:
            print(Exception('My NetERR', e))
            return None

        req_cookie = requests.utils.dict_from_cookiejar(loginSession.cookies)
        # print(res.status_code)
        # print(req_cookie)

        loginSession.close()
        return req_cookie

    def get_proxy(self, host, user):
        conn = pymongo.MongoClient(host=host, port=27017)
        db = conn['instagram']
        coll = db['instagram_account']
        for doc in coll.find():
            if doc['user'] == user:
                ip_address = doc['proxy']
                proxy_pass = doc['proxy_pass']
                proxy = ip_address+":"+proxy_pass
                return proxy

    def get_proxyEnable(self, host, user):
        conn = pymongo.MongoClient(host=host, port=27017)
        db = conn['instagram']
        coll = db['instagram_account']
        for doc in coll.find():
            if doc['user'] == user:
                proxyEnable = doc['proxyEnable']
                return proxyEnable


if __name__ == '__main__':
    # print('--------------Using requests--------------')

    url = 'https://instagram.com/jaychou/'
    test = Fetcher()
    host = sys.argv[1]
    myclient = pymongo.MongoClient(host, 27017)
    db = myclient['instagram']
    collections = db['instagram_account']
    user = sys.argv[2]
    collection = collections.find_one({"user": user})
    password = collection["password"]
    if test.get_proxyEnable(host, user):
        proxy = test.get_proxy(host, user)
        cookie = test.login_proxy(user, password, proxy)
        res = requests.get(url, params={}, headers=out_headers,
                           timeout=5, allow_redirects=False, cookies=cookie)
        if res.status_code != 200:
            status = 3
            tz = pytz.timezone('Asia/Shanghai')
            cookie_ban_timestamp = datetime.datetime.fromtimestamp(int(time.time()),
                                                                   pytz.timezone('Asia/Shanghai')).strftime(
                '%Y-%m-%d %H:%M:%S')
            collections.update_one(
                {"user": user}, {'$set': {'status': status, "cookie": cookie, "cookie_ban_timestamp": cookie_ban_timestamp}})
        else:
            status = 1
            collections.update_one(
                {"user": user}, {'$set': {'status': status, "cookie": cookie}})
    else:
        cookie = test.login(user, password)
        res = requests.get(url, params={}, headers=out_headers,
                           timeout=5, allow_redirects=False, cookies=cookie)
        if res.status_code != 200:
            status = 3
            tz = pytz.timezone('Asia/Shanghai')
            cookie_ban_timestamp = datetime.datetime.fromtimestamp(int(time.time()),
                                                                   pytz.timezone('Asia/Shanghai')).strftime(
                '%Y-%m-%d %H:%M:%S')
            collections.update_one(
                {"user": user},
                {'$set': {'status': status, "cookie": cookie, "cookie_ban_timestamp": cookie_ban_timestamp}})
        else:
            status = 1
            collections.update_one(
                {"user": user}, {'$set': {'status': status, "cookie": cookie}})
