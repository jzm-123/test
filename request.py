import datetime
import logging
import sys
import time

import pymongo
import pytz
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# class Fetcher(object):
#
#     def get_cookie(self, username, password):
#         options = Options()
#         options.add_argument("--headless")
#         driver = webdriver.Firefox(executable_path="C:\\Users\JinZhenming\AppData\Local\Programs\Python\Python38-32\geckodriver", options=options)
#         driver.get("https://www.instagram.com/accounts/login/")
#         # wait = WebDriverWait(driver, 60)
#         # try:
#         #     result = wait.until(EC.presence_of_all_elements_located((By.NAME, 'authenticity_token')))
#         # except TimeoutException:
#         #     print(">>>>>>>time out")
#         driver.find_element_by_name("username").send_keys(username)
#         # driver.find_element_by_name("session[password]").send_keys(password)
#         driver.find_element_by_name("password").send_keys(password)
#         driver.find_element_by_xpath('//button[@type="submit"]').click()
#         cookie_list = driver.get_cookies()
#         dic = {}
#         for cookie_item in cookie_list:
#             dic[cookie_item["name"]] = cookie_item["value"]
#         print(dic)
#         url = driver.current_url
#         driver.close()
#         driver.quit()
#         # redirect_url = "https://twitter.com/home"
#         redirect_url="https://www.instagram.com/"
#         if url == redirect_url:
#             self.whether_new_account = True
#             return dic
#         else:
#             return None
class Fetcher(object):

    def get_cookie(self, username, password):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path="C:\\Users\JinZhenming\AppData\Local\Programs\Python\Python38-32\geckodriver", options=options)
        driver.get("https://twitter.com/login")
        # wait = WebDriverWait(driver, 60)
        # try:
        #     result = wait.until(EC.presence_of_all_elements_located((By.NAME, 'authenticity_token')))
        # except TimeoutException:
        #     print(">>>>>>>time out")
        time.sleep(5)
        driver.find_element_by_name("session[username_or_email]").send_keys(username)
        driver.find_element_by_name("session[password]").send_keys(password)
        driver.find_element_by_xpath('//div[@data-testid="LoginForm_Login_Button"]').click()
        cookie_list = driver.get_cookies()
        dic = {}
        for cookie_item in cookie_list:
            dic[cookie_item["name"]] = cookie_item["value"]
        url = driver.current_url
        driver.close()
        driver.quit()
        redirect_url = "https://twitter.com/home"
        if url == redirect_url:
            self.whether_new_account = True
            return dic
        else:
            return None

if __name__ == "__main__":
    test = Fetcher()
    cookie=test.get_cookie("861959219@qq.com","19971109.Jzmy")
    print(cookie)
    # logging.basicConfig(filename='twitter_cookie.log', level=logging.DEBUG)
    # test = Fetcher()
    # host = sys.argv[1]
    # conn = pymongo.MongoClient(host, 27017)
    # db = conn['twitter']
    # collections = db['twitter_account']
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
