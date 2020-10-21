# -*- coding: utf-8 -*-
from urllib import parse
from Distributed_instagram_spider.items import *
from Distributed_instagram_spider.util.ins_setting import *
from scrapy_redis.spiders import RedisSpider


class C_SonComments(RedisSpider):
    name = 'soncomments'
    redis_key = 'soncomments:start_urls'
    base_url = 'https://www.instagram.com/graphql/query/?query_hash={0}&variables={1}'

    def __init__(self, redis_url=None, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(C_SonComments, self).__init__(*args, **kwargs)
        self.redis_url = redis_url

    def parse(self, response):
        j = json.loads(response.text)
        list = j["data"]["comment"]["edge_threaded_comments"]["edges"]
        parent_id = j["data"]["comment"]["id"]
        for i in list:
            son_comment = SonComments(id=i["node"]["id"], user_id=i["node"]["owner"]["id"],
                                      username=i["node"]["owner"]["username"]
                                      , content=i["node"]["text"], time=i["node"]["created_at"],
                                      likes=i["node"]["edge_liked_by"]["count"], parent_id=parent_id)
            yield son_comment
        has_next_page = j["data"]["comment"]["edge_threaded_comments"]["page_info"]["has_next_page"]
        if has_next_page:
            after = j["data"]["comment"]["edge_threaded_comments"]["page_info"]["end_cursor"]
            vars = {"comment_id": parent_id, "first": 50, "after": after}
            text = json.dumps(vars)
            url = self.base_url.format(query_hash5, parse.quote(text))
            InsertToRedis('soncomments:start_urls', url, self.redis_url)
