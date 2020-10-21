# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['Distributed_instagram_spider.spiders']
NEWSPIDER_MODULE = 'Distributed_instagram_spider.spiders'


#指定使用scrapy-redis的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#指定使用scrapy-redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 默认的 按优先级排序(Scrapy默认)，由sorted set实现的一种非FIFO、LIFO方式。
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
SCHEDULER_PERSIST = True

#默认情况下,RFPDupeFilter只记录第一个重复请求。将DUPEFILTER_DEBUG设置为True会记录所有重复的请求。
DUPEFILTER_DEBUG =True

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

DOWNLOADER_MIDDLEWARES  = {
    # 该中间件将会收集失败的页面，并在爬虫完成后重新调度。（失败情况可能由于临时的问题，例如连接超时或者HTTP 500错误导致失败的页面）
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 80,
    # 该中间件提供了对request设置HTTP代理的支持。您可以通过在 Request 对象中设置 proxy 元数据来开启代理。
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
    #该中间件提供了对request设置cookie代理的支持
    'Distributed_instagram_spider.middlewares.CookiesMiddleware':300,
    #该中间件提供了对request设置user_agent代理的支持
    'Distributed_instagram_spider.middlewares.RandomUserAgent':200,
    #该中间件提供了对request设置proxy代理的支持
    # 'Distributed_instagram_spider.middlewares.ProxyMiddleware':543,
    # 'example.middlewares.ProcessAllExceptionMiddleware': 543,
    # 'example.middlewares.RotateUserAgentMiddleware': 200,
    'Distributed_instagram_spider.middlewares.ProxyMiddleware': 100,
}

ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300,
    # 'Distributed_instagram_spider.pipelines.MongoPipeline': 301,
}

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' ,
    "Origin": "https://www.instagram.com",
    'Referer': 'https://www.instagram.com/instagram/',
    'upgrade-insecure-requests': '1',
}

#日志等级
LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 3
REDIS_URL = 'redis://127.0.0.1:6379'






