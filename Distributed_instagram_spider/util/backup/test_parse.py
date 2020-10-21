import re

f = open('E:/PycharmProjects/Spider/Distributed_twitter_spider/Distributed_twitter_spider/util/url.txt','rb')
res = f.read()
# print(res)
f.close()



# articles_pattern = re.compile(r'<article.+?</article>')
# articles = re.findall(articles_pattern, res.decode('utf-8'))
# print('articles:',articles)
# <a href="tel:+886223113731">

tel_pattern = re.compile(r'<a href="tel:(.*?)">')
tel = re.findall(tel_pattern,res.decode('utf-8'))[0]
# print('tel:',tel)

basic_info_pattern = re.xpath('./div[@class=]')




