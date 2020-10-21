# -*- coding: utf-8 -*-
import requests
from urllib import parse
from Distributed_instagram_spider.items import *
from Distributed_instagram_spider.util.ins_setting import *
from scrapy_redis.spiders import RedisSpider


class C_Posts(RedisSpider):
    name = 'posts'
    redis_key = 'posts:start_urls'
    base_url = 'https://www.instagram.com/graphql/query/?query_hash={0}&variables={1}'

    def __init__(self, redis_url=None, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(C_Posts, self).__init__(*args, **kwargs)
        self.redis_url = redis_url


    def parse(self, response):
        j = json.loads(response.text)
        list = j["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
        user_id=list[0]["node"]["owner"]["id"]
        for i in list:
            node = i["node"]  # 一个帖子结点
            shortcode = node["shortcode"]
            post = Posts(id=node["id"], url=node["display_url"],
                         content=node["edge_media_to_caption"]["edges"][0]["node"]["text"]
                         , time=node["taken_at_timestamp"], likes=node["edge_media_preview_like"]["count"],
                         comment_num=node["edge_media_to_comment"]["count"]
                         , user_id=user_id, shortcode=shortcode, is_video=node["is_video"])
            yield post
            if not node["is_video"]:
                attempts = 0
                flag = True
                while attempts < 2 and flag:
                    try:
                        r = requests.get(node["display_url"], timeout=2)
                        post = Image(picture_id=node["id"], picture_url=node["display_url"], post_id=node["id"],user_id=user_id,content=r.content)
                        yield post
                        flag = False
                    except:
                        attempts += 1
                        # print("download " + node["id"] + "failed,try "+str(attempts))
            # 评论页面查询
            vars = {"shortcode": shortcode, "first": 50}
            text = json.dumps(vars)
            url = self.base_url.format(query_hash4, parse.quote(text))
            InsertToRedis('comments:start_urls', url, self.redis_url)
            if "edge_sidecar_to_children" in node:
                sons = node["edge_sidecar_to_children"]["edges"][1:]  # 第一个是父结点,跳过
                # 子稿件查询
                for son in sons:
                    post = PostsSon(son_id=son["node"]["id"], son_url=son["node"]["display_url"]
                                       , son_is_video=son["node"]["is_video"])
                    yield post
                    if not son["node"]["is_video"]:
                        attempts = 0
                        flag = True
                        while attempts < 2 and flag:
                            try:
                                r = requests.get(son["node"]["display_url"], timeout=2)
                                post = Image(id=son["node"]["id"], url=son["node"]["display_url"],  content=r.content)
                                yield post
                                flag = False
                            except:
                                attempts += 1
                                # print("download " + son["node"]["id"] + "failed,try "+str(attempts))
        # 查询下一页帖子
        has_next_page = j["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]
        if has_next_page:
            after = j["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
            vars = {"id": user_id, "first": 50, "after": after}
            text = json.dumps(vars)
            url = self.base_url.format(query_hash3, parse.quote(text))
            InsertToRedis('posts:start_urls', url, self.redis_url)
