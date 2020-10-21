# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from Distributed_instagram_spider.util.ins_setting import *
import base64
import random

# cookie Middleware
class CookiesMiddleware(object):
    def process_request(self, request, spider):
        cookie = random.choice(get_cookies(HOST))
        request.cookies = cookie


# user_agent Middleware
class RandomUserAgent(object):
    def process_request(self, request, spider):
        agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', agent)


# proxy middle
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxyEnable = get_proxyEnable(HOST, request.cookies)
        if proxyEnable == True:
            request.meta['proxy'] = get_proxy(HOST, request.cookies)
            proxy_name_pass = get_proxy_pass(HOST, request.cookies)
            encode_pass_name = base64.b64encode(proxy_name_pass)
            request.headers['Proxy-Authorization'] = 'Basic ' + encode_pass_name.decode()
