# -*- coding: utf-8 -*-
import urllib
from urllib import parse
from Distributed_instagram_spider.items import *
from Distributed_instagram_spider.util.ins_setting import *
from scrapy_redis.spiders import RedisSpider


class C_Comments(RedisSpider):
    name = 'comments'
    redis_key = 'comments:start_urls'
    base_url = 'https://www.instagram.com/graphql/query/?query_hash={0}&variables={1}'

    def __init__(self, redis_url=None, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(C_Comments, self).__init__(*args, **kwargs)
        self.redis_url = redis_url

    def parse(self, response):
        j = json.loads(response.text)
        list = j["data"]["shortcode_media"]["edge_media_to_parent_comment"]["edges"]
        o = urllib.parse.urlparse(response.url)
        a = urllib.parse.parse_qs(o.query)
        post_shortcode = json.loads(a["variables"][0])["shortcode"]  # shortcode与帖子一一对应
        for i in list:
            comment = Comments(id=i["node"]["id"], user_id=i["node"]["owner"]["id"],
                               username=i["node"]["owner"]["username"]
                               , content=i["node"]["text"], time=i["node"]["created_at"],
                               likes=i["node"]["edge_liked_by"]["count"]
                               , post_shortcode=post_shortcode, son_comments=i["node"]["edge_threaded_comments"]["count"])
            yield comment
            if comment["son_comments"]:
                vars = {"comment_id": comment["id"], "first": 50}
                text = json.dumps(vars)
                url = self.base_url.format(query_hash5, parse.quote(text))
                InsertToRedis('soncomments:start_urls', url, self.redis_url)
        has_next_page = j["data"]["shortcode_media"]["edge_media_to_parent_comment"]["page_info"]["has_next_page"]
        if has_next_page:
            after = j["data"]["shortcode_media"]["edge_media_to_parent_comment"]["page_info"]["end_cursor"]
            vars = {"shortcode": post_shortcode, "first": 50, "after": after}
            text = json.dumps(vars)
            url = self.base_url.format(query_hash4, parse.quote(text))
            InsertToRedis('comments:start_urls', url, self.redis_url)
