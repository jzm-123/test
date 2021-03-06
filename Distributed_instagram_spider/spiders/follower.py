# -*- coding: utf-8 -*-
import urllib
from urllib import parse
from Distributed_instagram_spider.items import *
from Distributed_instagram_spider.util.ins_setting import *
from scrapy_redis.spiders import RedisSpider


class C_Follower(RedisSpider):
    name = 'follower'
    redis_key = 'follower:start_urls'
    base_url = 'https://www.instagram.com/graphql/query/?query_hash={0}&variables={1}'

    def __init__(self, redis_url=None, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(C_Follower, self).__init__(*args, **kwargs)
        self.redis_url = redis_url

    def parse(self, response):
        j = json.loads(response.text)
        list = j["data"]["user"]["edge_followed_by"]["edges"]
        o = urllib.parse.urlparse(response.url)
        a = urllib.parse.parse_qs(o.query)
        user_id = json.loads(a["variables"][0])["id"]
        for i in list:
            follower = Followers(id=i["node"]["id"], follower_name=i["node"]["username"], user_id=user_id);
            yield follower
            url = "http://www.instagram.com/" + i["node"]["username"]
            InsertToRedis('userinfo:start_urls', url, self.redis_url)
        has_next_page = j["data"]["user"]["edge_followed_by"]["page_info"]["has_next_page"]
        if has_next_page:
            after = j["data"]["user"]["edge_followed_by"]["page_info"]["end_cursor"]
            vars = {"id": user_id, "first": 50, "include_reel": "false", "after": after}
            text = json.dumps(vars)
            url = self.base_url.format(query_hash, parse.quote(text))
            InsertToRedis('follower:start_urls', url, self.redis_url)
