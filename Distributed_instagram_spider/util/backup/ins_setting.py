import pymongo
import redis
import json

def _getFirstItem(items):
    return items[0] if len(items) > 0 else None


def _parseNumStr2Int(numStr):
    if not numStr:
        return 0
    numStr = numStr.replace(',', '')
    if numStr.find('K') > -1:
        numStr = numStr.replace('K', '')
        return int(float(numStr) * 1000)
    elif numStr.find('M') > -1:
        numStr = numStr.replace('M', '')
        return int(float(numStr) * 1000000)
    elif numStr.find('千') != -1:
        numStr = numStr.replace('千', '')
        return int(float(numStr) * 1000)
    elif numStr.find('万') != -1:
        numStr = numStr.replace('万', '')
        return int(float(numStr) * 10000)
    else:
        return int(numStr)

#检查城市是否是台湾地区的城市
def check_conatincity_taiwan(city_name):
    if city_name in city_items:
        return True
    else:
        return False

#取得爬虫所选取的ip代理,并且删除已经过时的代理IP
def get_twitter_ip_address():
    client = pymongo.MongoClient('10.1.18.93', 27017)
    TwitterSpider = client['twitter']
    twitter_ip_address_collect = TwitterSpider['IP_Address']
    ip_list = []
    for ip_address in twitter_ip_address_collect.find():
        del ip_address['_id']
        ip_list.append(ip_address)
    return ip_list

#取得登录所需要的cookies
def get_twitter_cookies():
    conn = pymongo.MongoClient('127.0.0.1', 27017)
    db = conn['twitter']
    twitter_cookie_collection = db['cookie_update']
    cookies = []
    for twitter_cookie in twitter_cookie_collection.find():
        cookies.append(twitter_cookie['cookie'])
    return cookies

#将随机表中的cookie所对应的account返回出来
def get_cookie_account(cookie):
    conn = pymongo.MongoClient('127.0.0.1', 27017)
    db = conn['twitter']
    twitter_cookie_collection = db['cookie_update']

    for twitter_cookie in twitter_cookie_collection.find():
        if twitter_cookie['cookie']== cookie:
            return twitter_cookie['account']

#向redis数据库中插入任务队列
def InsertToRedis(name,value):
    r = redis.Redis(host='10.1.18.93',port='6379')
    # r = redis.Redis(host='127.0.0.1',port=6379)
    r.lpush(name,value)

def AddRedis(name,value):
    r = redis.Redis(host='10.1.18.93', port='6379')
    result = json.dumps(value)
    r.lpush(name,result)


PROXIES = get_twitter_ip_address()
# PROXIES = {'HTTP':'75.151.213.85:8080','HTTP':'159.138.22.112:80'}
# PROXIES = ['HTTP:']
COOKIES = get_twitter_cookies()
# COOKIES = [{'_twitter_sess': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJ%252FiXXhnAToMY3NyZl9p%250AZCIlODNkMTMwZmRkY2E1NmFhZGFkMGFhNzgxMGRlYzhmY2Q6B2lkIiVkOGU3%250AOTk2YzhkODg4MDNmMTkyYjY5MjU2ZGM1ZmMyNDoJdXNlcmwrCQBgFKkjknwO--78d370adccdb325773317247efe875403ff13ab8', 'ads_prefs': '"HBISAAA="', 'auth_token': '0fa89aa8d2feb63c274f426a660e590b3f20422d', 'csrf_same_site': '1', 'csrf_same_site_set': '1', 'ct0': '6603ee82d955573bd06faaf48dfbef95', 'dnt': '1', 'guest_id': 'v1%3A154391267804465303', 'kdt': '5nqe2n9OJ3ozLzCFVzqvRsJCmy982hFmrbTQkCjx', 'personalization_id': '"v1_Kqa0wqNrA5MyH43Xw0v8tQ=="', 'remember_checked_on': '1', 'twid': '"u=1043869895501307904"', 'lang': 'zh-cn'}]
#分布式推特爬虫的user_agents
USER_AGENTS = ['Mozilla/5.0 (Windows NT 6.3; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
             'Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.00',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
]
#台湾地区各大县市的名称
CITYS = {
        '台湾':['Taiwan','台灣','台湾','台灣省','台湾省'],
        '台北':['Taipei City','台北市, 台灣','台北','台北市','Taipei,Taiwan','Taipei,Taiwan ROC'],
        '新北':['New Taipei City','新北市, 台灣','新北','新北市 '],
        '桃园':['Taoyuan City','桃園縣, 台灣','桃园市','桃園市','桃园','桃園'],
        '台中':['Taichung City','台中市, 台灣','台中','台中市'],
        '台南':['Tainan City','台南市, 台灣','台南','台南市'],
        '高雄':['Kaohsiung City','高雄市, 台灣','高雄市','高雄'],
        '基隆':['Keelung City','基隆市, 台灣','基隆市','基隆'],
        '新竹':['Hsinchu City','新竹市, 台灣','新竹市','新竹'],
        '嘉义':['Chiayi City','嘉義市, 台灣','嘉义','嘉义市','嘉義','嘉義市'],
        '新竹县':['Hsinchu County','新竹縣, 台灣','新竹县'],
        '苗栗县':['Miaoli County','苗栗縣, 台灣','苗栗县','苗栗'],
        '彰化县':['Changhua County','彰化縣, 台灣','彰化县','彰化县'],
        '南投县':['Nantou County','南投縣, 台灣','南投县','南投'],
        '云林县':['Yunlin County','雲林縣, 台灣','云林县','云林','雲林縣','雲林'],
        '嘉义县':['Chiayi County','嘉義縣, 台灣','嘉义县'],
        '屏东县':['Pingtung County','屏東縣, 台灣','屏東縣','屏东县','屏东','屏東'],
        '宜兰县':['Yilan County','宜蘭縣, 台灣','宜兰县','宜蘭','宜兰'],
        '花莲县':['Hualien County','花蓮縣, 台灣','花莲县','花蓮縣','花蓮','花莲'],
        '台东县':['Taitung County','台東縣, 台灣','台東縣','台東縣','台东县','台东'],
        '澎湖县':['Penghu County','澎湖縣, 台灣','澎湖縣','澎湖','澎湖县'],
        '金门县':['Kinmen County','金門縣, 台灣','金門縣','金門','金门县','金门'],
        '连江县':['Lienchiang County','連江縣, 台灣','連江縣','連江','连江县','连江']
    }
#推特中各大县市的名称
city_items = ['Taiwan', '台灣', '台湾', '台灣省', '台湾省',' Taiwan,Tainan','台灣Taiwan台湾','台湾',
              'TaipeiCity', '台北市,台灣', '台北', '台北市', 'Taipei,Taiwan','台北市Taiwan','Taiwan台灣','Taipei',
              'Taipei,TaiwanROC','中華民國臺北市','TaipeiCity,Taiwan(NOTCHINA)','TaipeiCity,Taiwan',
              'NewTaipeiCity','新北市,台灣', '新北', '新北市 ','新北市,台灣',
              'TaoyuanCity', '桃園縣,台灣', '桃园市', '桃園市', '桃园', '桃園',
              'TaichungCity', '台中市,台灣', '台中', '台中市','海外　台湾',
              'TainanCity', '台南市,台灣', '台南', '台南市','TaichungCity,Taiwan'
              'KaohsiungCity','高雄市,台灣', '高雄市', '高雄','高雄的岡山',
              'KeelungCity', '基隆市,台灣', '基隆市', '基隆',
              'HsinchuCity', '新竹市,台灣', '新竹市', '新竹',
              'ChiayiCity', '嘉義市,台灣', '嘉义', '嘉义市', '嘉義', '嘉義市',
              'HsinchuCounty', '新竹縣,台灣', '新竹县',
              'MiaoliCounty', '苗栗縣,台灣', '苗栗县', '苗栗',
              'ChanghuaCounty', '彰化縣,台灣', '彰化县', '彰化县',
              'NantouCounty', '南投縣,台灣', '南投县', '南投',
              'YunlinCounty', '雲林縣,台灣', '云林县', '云林', '雲林縣', '雲林',
              'ChiayiCounty', '嘉義縣,台灣', '嘉义县', 'PingtungCounty', '屏東縣, 台灣', '屏東縣', '屏东县', '屏东', '屏東',
              'YilanCounty', '宜蘭縣,台灣', '宜兰县', '宜蘭', '宜兰',
              'HualienCounty', '花蓮縣,台灣', '花莲县', '花蓮縣', '花蓮', '花莲',
              'TaitungCounty', '台東縣,台灣', '台東縣', '台東縣', '台东县', '台东',
              'PenghuCounty', '澎湖縣,台灣', '澎湖縣', '澎湖', '澎湖县',
              'KinmenCounty', '金門縣,台灣', '金門縣', '金門', '金门县', '金门',
              'LienchiangCounty', '連江縣,台灣', '連江縣', '連江', '连江县', '连江'
              'taiwan','台灣台東縣','Taipei','Tainan,Taiwan','台北帝国大学','TaipeiCity,Taiwan','台南市(Tainan)','TaipeiTaiwan',
                'Taichung,Taiwan','高雄市,台灣','Taiwan-Taichung','KaohsiungCity,Taiwan','Taiwan','中華帝國','台灣省花蓮',
              '台北市,台灣','Taiwan,TaipeCity'
              ]
# 推特请求头
Twitter_HEADER = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                  "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                  "Accept-Encoding": "gzip, deflate, br",
                  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                  "Host": "twitter.com",
                  "Origin": "https://twitter.com",
                  # "X-Requested-With": "XMLHttpRequest",
                  # "X-Twitter-Active-User": "yes",
                  # "X-Twitter-Polling": "true",
               }
# 睡眠延时
SLEEP_TIME = 1
# 线程数目
WORKERS = 7
# 节点数目
NODES_SUM = 3
# 当前节点序号
NUM = 0
START_LIST=[
    'iingwen',
    'PresidentMa19',
    'thecarol',
    'ctba',
    'DPPonline',
    'HSBC_TW',
    'foreignersinTW'
]

