# -*- coding: utf-8 -*-
import logging
import re
from datetime import datetime
from urllib import parse

import pytz

from Distributed_instagram_spider.items import *
from Distributed_instagram_spider.util.ins_setting import *
from scrapy_redis.spiders import RedisSpider
import time


class C_UserInfo(RedisSpider):
    name = 'instagram_userinfo'
    redis_key = 'instagram_userinfo:start_urls'
    base_url = 'https://www.instagram.com/graphql/query/?query_hash={0}&variables={1}'
    def __init__(self, redis_url=None, followHop=None,followingHop=None,followConfig=None,followingConfig=None,
                 postConfig=None, job_id=None, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(C_UserInfo, self).__init__(*args, **kwargs)
        self.followConfig = int(followConfig)
        self.followingConfig=int(followingConfig)
        self.followHop=followHop
        self.followingHop=followingHop
        self.redis_url = redis_url
        self.job_id = job_id
        self.postConfig = int(postConfig)

    def parse(self, response):
        Cookie = response.request.headers.getlist('Cookie')
        if response.status == 200:
            p1 = re.compile(r'window._sharedData = (.*?);</script>', re.MULTILINE)
            j1 = re.findall(p1, response.text)[0]
            l1 = json.loads(j1)  # l1为sharedData中的json格式数据
            userinfo = l1["entry_data"]["ProfilePage"][0]["graphql"]["user"]
            if userinfo:
                main_site = 'https://www.instagram.com/' + userinfo["username"] + '/'
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                timestamp_int = int(time.time() * 1000)
                user_id=userinfo["id"]
                profile_pic_url = userinfo["profile_pic_url"]
                if profile_pic_url:
                    image_name = '../util/instagram_images/user/' + str(self.job_id) + '/' + str(
                        user_id) + '/' + 'userinfo' + '/' + str(user_id) + '.jpg'
                    image_path = '../util/instagram_images/user/' + str(self.job_id) + '/' + str(
                        user_id) + '/' + 'userinfo'
                    image_temp = str(user_id) + '.jpg'
                    image_status = {"jobId": self.job_id, "type": "userinfo", "userId": user_id,
                                    "fileName": image_temp, "status": 0}
                    urllib_download(profile_pic_url, image_path, image_name, image_status)
                business_account =''
                if "business_account" in userinfo:
                    business_account=userinfo["business_account"]
                user = UserInfo(timestamp=timestamp,timestampInt=timestamp_int,user_id=userinfo["id"], username=userinfo["username"], biography=userinfo["biography"],
                                posts_num=userinfo["edge_owner_to_timeline_media"]["count"],
                                follower_num=userinfo["edge_followed_by"]["count"],
                                following_num=userinfo["edge_follow"]["count"], is_verified=userinfo["is_verified"],
                                external_url=userinfo["external_url"],
                                external_url_linkshimmed=userinfo["external_url_linkshimmed"],
                                is_business_account=userinfo["is_business_account"],
                                is_joined_recently=userinfo["is_joined_recently"],
                                profile_pic_url=userinfo["profile_pic_url"],
                                business_account=business_account,
                                site=main_site)
                # spider_name = 'userinfo'
                # key = 'url'
                # value = response.url
                periodic_times = get_periodic_from_redis(self.redis_url)
                # if periodic_times:
                user["periodic_times"] = periodic_times
                # tz = pytz.timezone('Asia/Shanghai')
                # cookie_timestamp = datetime.datetime.fromtimestamp(int(time.time()), tz).strftime(
                #     '%Y-%m-%d %H:%M:%S')
                # json_str = {"spider_name": "userinfo", "url": response.url, "status": 1,
                #             "timestamp": cookie_timestamp, "instagram_periodic": periodic_times}
                # # spider_name = 'userinfo'
                # # key = 'url'
                # # value = response.url
                # UpdateInfo(self.redis_url, spider_name, key, value, json_str)
                logging.debug(user)
                yield user
                vars = {"id": userinfo["id"], "first": 50, "include_reel": "false"}
                text = json.dumps(vars)
                url = self.base_url.format(query_hash, parse.quote(text))
                InsertToRedis('instagram_follower:start_urls', url, self.redis_url)
                url2 = self.base_url.format(query_hash2, parse.quote(text))
                InsertToRedis('instagram_following:start_urls', url2, self.redis_url)
                vars = {"id": userinfo["id"], "first": 50}
                text = json.dumps(vars)
                url3 = self.base_url.format(query_hash3, parse.quote(text))
                InsertToRedis('instagram_posts:start_urls', url3, self.redis_url)

