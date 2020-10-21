import pymongo
import requests
import re
import json
import os

session = requests.session()
"""
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/skillCategory?includeHiddenEndorsers=True
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/browsemapWithDistance
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/profileContactInfo
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/+ experience_id + "/positionGroups?start=0&count=" + str(experience_count)
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/
"""
class Fetcher(object):

    def __init__(self):
        self.loginUrl = "https://www.instagram.com/accounts/login/ajax/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0" }

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


if __name__ == "__main__":
    test = Fetcher()
    # cookie = test.login("861959219@qq.com", "19971109.Jzmy")
    if not os.path.isfile("cookie.json"):
        cookie = test.login("1652599079", "19971109.Jzmy")
        print(cookie)
        with open("cookie.json", 'w') as f:
            json.dump(cookie, f)
    else:
        with open("cookie.json", 'r') as f:
            cookie = json.load(f)



