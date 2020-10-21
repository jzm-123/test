import re

f = open('E:/PycharmProjects/Spider/Distributed_twitter_spider/Distributed_twitter_spider/util/新建文本文档.txt')
res = f.read()
# print(res)
f.close()
# print(res)
urlpattern = re.compile(r'<GET https://twitter.com/account/access> from <GET https://twitter.com/(.*?)/>')
urls = re.findall(urlpattern,res)
print('url:',urls)
print(len(urls))
for url in urls:
    # print('url:',url)
    https = "lpush twitter_user_info_spider:start_urls http://twitter.com/"+url+"/"
    # print(https)
    f1 = open('../util/url_01_09.txt','a+')
    f1.write(https)
    f1.write('\n')
f1.close()