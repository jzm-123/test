# -*- coding: utf-8 -*-
import re
from urllib import parse
from Distributed_instagram_spider.items import *
from Distributed_instagram_spider.util.ins_setting import *
from scrapy_redis.spiders import RedisSpider



class C_UserInfo(RedisSpider):
    name = 'userinfo'
    redis_key = 'userinfo:start_urls'
    base_url = 'https://www.instagram.com/graphql/query/?query_hash={0}&variables={1}'

    def __init__(self, redis_url=None, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(C_UserInfo, self).__init__(*args, **kwargs)
        self.redis_url = redis_url

    def parse(self, response):
        p1 = re.compile(r'window._sharedData = (.*?);</script>', re.MULTILINE)
        j1 = re.findall(p1, response.text)[0]
        l1 = json.loads(j1)  # l1为sharedData中的json格式数据
        userinfo = l1["entry_data"]["ProfilePage"][0]["graphql"]["user"]
        main_site = 'https://www.instagram.com/' + userinfo["username"] + '/'
        user = UserInfo(id=userinfo["id"], username=userinfo["username"], biography=userinfo["biography"],
                        posts_num=userinfo["edge_owner_to_timeline_media"]["count"],
                        follower_num=userinfo["edge_followed_by"]["count"],
                        following_num=userinfo["edge_follow"]["count"], is_verified=userinfo["is_verified"],
                        external_url=userinfo["external_url"],external_url_linkshimmed=userinfo["external_url_linkshimmed"],
                        is_business_account=userinfo["is_business_account"],is_joined_recently=userinfo["is_joined_recently"],
                        profile_pic_url=userinfo["profile_pic_url"],business_account=userinfo["business_account"],site=main_site)
        yield user
        vars = {"id": userinfo["id"], "first": 50, "include_reel": "false"}
        text = json.dumps(vars)
        url = self.base_url.format(query_hash, parse.quote(text))
        InsertToRedis('follower:start_urls', url, self.redis_url)
        url2 = self.base_url.format(query_hash2, parse.quote(text))
        InsertToRedis('following:start_urls', url2, self.redis_url)
        vars = {"id": userinfo["id"], "first": 50}
        text = json.dumps(vars)
        url3 = self.base_url.format(query_hash3, parse.quote(text))
        InsertToRedis('posts:start_urls', url3, self.redis_url)

