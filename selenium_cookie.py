import datetime
import json
import logging
import sys
import time
from threading import Thread

import pymongo
import pytz
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Fetcher(object):
    def get_cookie(self, username, password):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path="C:\\Users\JinZhenming\AppData\Local\Programs\Python\Python38-32\geckodriver", options=options)
        driver.get("https://www.instagram.com/accounts/login/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(
            username)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        cookie_list = driver.get_cookies()
        dic = {}
        for cookie_item in cookie_list:
            dic[cookie_item["name"]] = cookie_item["value"]
        url = driver.current_url
        driver.close()
        driver.quit()
        return dic
        # print(url)
        # print(dic)
        # redirect_url="https://www.instagram.com/"
        # if url == redirect_url:
        #     self.whether_new_account = True
        #     return dic
        # else:
        #     return None
if __name__ == "__main__":
    test = Fetcher()
    loginUrl="https://www.instagram.com/jaychou/"
    url1='https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables=%7B%22id%22%3A%20%224055534935%22%2C%20%22first%22%3A%2050%2C%20%22include_reel%22%3A%20%22false%22%7D'
    url='https://www.instagram.com/graphql/query/?query_hash=7da1940721d75328361d772d102202a9&variables=%7B%22shortcode%22%3A%22CFbBrXbjWJl%22%2C%22child_comment_count%22%3A3%2C%22fetch_comment_count%22%3A40%2C%22parent_comment_count%22%3A24%2C%22has_threaded_comments%22%3Atrue%7D'
    url2='https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables=%7B%22id%22%3A%20%224055534935%22%2C%20%22first%22%3A%2050%2C%20%22include_reel%22%3A%20%22false%22%7D'
    cookie=test.get_cookie("16.52599079","19971109.Jzmy")
    print(cookie)
    
    
    # logging.basicConfig(filename='instagram_cookie.log', level=logging.DEBUG)
    # test = Fetcher()
    # host = sys.argv[1]
    # conn = pymongo.MongoClient(host, 27017)
    # db = conn['instagram']
    # collections = db['instagram_account']
    # user = sys.argv[2]
    # collection = collections.find_one({"user": user})
    # password = collection["password"]
    # cookie = test.get_cookie(user, password)
    # if not cookie:
    #     status = 3
    #     tz = pytz.timezone('Asia/Shanghai')
    #     cookie_ban_timestamp = datetime.datetime.fromtimestamp(int(time.time()),
    #                                                            pytz.timezone('Asia/Shanghai')).strftime(
    #         '%Y-%m-%d %H:%M:%S')
    #     collections.update_one(
    #         {"user": user},
    #         {'$set': {'status': status, "cookie": cookie, "cookie_ban_timestamp": cookie_ban_timestamp}})
    # else:
    #     status = 1
    #     collections.update_one(
    #         {"user": user},
    #         {'$set': {'status': status, "cookie": cookie, "whether_new_account": test.whether_new_account}})
    #     collections.update_one({"user": user}, {'$unset': {'cookie_ban_timestamp': ""}})
    url3="https://www.instagram.com/jaychou?__a=1"
    payload = {
        "username": "16.52599079",
        "password": "19971109.Jzmy",
        "queryParams": "{\"source\": \"auth_switcher\"}",
        "optIntoOneTap": "true"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    out_headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                   "Host": "www.instagram.com",

                   }
    res = requests.get(url3, params={}, headers=out_headers,
                       timeout=5, allow_redirects=False, cookies=cookie)
    # print(res.text)
    # with open("inster_follow.txt", 'w',encoding='UTF-8') as f:
    #     f.write(res.text)
    print(res.status_code)
