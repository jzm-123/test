from pymongo import MongoClient
import re
import sys
import requests
import pymongo


out_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                   # "Cookie": 'personalization_id="v1_BrIrRp6TXQ/nf+8SdEjPjw=="; guest_id=v1%3A154043699389757049; _ga=GA1.2.2083014965.1540437000; tfw_exp=0; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCCqlHVlnAToHaWQiJWNm%250ANmNlZjM5NzJmZTkxMzlmMmFiOGM5MzU1ZDAwMDhlOgxjc3JmX2lkIiVjM2Vi%250AYTQ3ZTgxZjJjZmExY2U5ZmJkNGY3MTVjOTk2ZjoJdXNlcmwrCQAAVfM1Kt0J--dd67bf5e2b5f48babf7f45f3ce29cc00852c0cc8; _gid=GA1.2.2003646199.1543459187; ads_prefs="HBERAAA="; kdt=PiJw5JxUUfKjulipUbrmEw4t9uXZvx4JzgDQnMdF; remember_checked_on=1; twid="u=710770727398473728"; auth_token=05982ff852fedda922a5f87742c6ed7447d057d6; csrf_same_site_set=1; lang=zh-cn; csrf_same_site=1; _mobile_sess=BAh7ByIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNoSGFzaHsABjoKQHVzZWR7ADoQX2NzcmZfdG9rZW4iLWRiNzdmMmI3MmY3ZDQ4M2U0ZDRkMjllZjAzMThkMmIyZDdjMzcyYTQ%3D--41d366bf90113c941efc9dc32e6a0581ae7a6d3f; mobile_metrics_token=154346182042177713; u=fbb62c4de1377094413f86e4097712a1c8515afd; mbox=session#b753aaa4bd4a4beb8bbd1f2dbce52c02#1543481564|PC#b753aaa4bd4a4beb8bbd1f2dbce52c02.28_78#1544689304|check#true#1543479764; fontsLoaded=true; ct0=3780c5cce98a0a7892afa428beb6d657',
                   "Host": "twitter.com",
                   "Origin": "https://twitter.com",
                   # "X-Requested-With": "XMLHttpRequest",
                   # "X-Twitter-Active-User": "yes",
                   # "X-Twitter-Polling": "true",
                   }



class Fetcher(object):

    def __init__(self):
        self.loginUrl = 'https://twitter.com/login'
        self.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                   'Host': 'twitter.com',}



    def login(self,username,password):
        loginSession = requests.Session()
        try:
            print('http requests ing ... ', self.loginUrl)
            res = loginSession.get(self.loginUrl, verify=False, timeout=30, allow_redirects=False)
            # print('http requests done ... ', res.url)
        except Exception as e:
            print(e)
            return None

        html = res.text
        # from bs4 import BeautifulSoup as bs
        # soup = bs(html,'lxml')

        authenticity_token = re.search(r'name="authenticity_token" value="(.+?)"', html).group(1)
        print('authenticity_token:', authenticity_token)
        # at = soup.select('input[name="authenticity_token"]')[0]
        # print(at)

        # ui_metrics = re.search(r'name="ui_metrics" value="(.+?)"', html).group(1)
        # ui_metrics = soup.select('input[name="ui_metrics"]')
        # for u in ui_metrics:
        #     print('ui_metrics:', u)

        payload = {'session[username_or_email]': username,
                   'session[password]': password,
                   'authenticity_token': authenticity_token,
                   'scribe_log':'',
                   'remember_me': '1',

                   'redirect_after_login': '',
                   }
        # userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
        # headers = {'User-Agent': userAgent,
        #            'Accept-Encoding': 'gzip, deflate, br',
        #            'Accept-Language': 'zh-CN,zh;q=0.8',
        #            'X-Requested-With': 'XMLHttpRequest'}
        url = 'https://twitter.com/sessions'
        try:
            print('http requests ing ... ', url)
            res = loginSession.post(url, verify=False, headers=self.headers, data=payload, timeout=30, allow_redirects=True)
            print('http requests done ... ', res.url)
        except Exception as e:
            print(Exception('My NetERR', e))
            return None

        req_cookie = requests.utils.dict_from_cookiejar(loginSession.cookies)

        # print(req_cookie)

        loginSession.close()
        return req_cookie

    def login_proxy(self,username,password,proxies):
        loginSession = requests.Session()
        loginSession.proxies = proxies
        try:
            # print('http requests ing ... ', self.loginUrl)
            res = loginSession.get(self.loginUrl, verify=False, timeout=30, allow_redirects=False)
            print('http requests done ... ', res.url)
        except Exception as e:
            print(e)
            return None

        html = res.text
        # from bs4 import BeautifulSoup as bs
        # soup = bs(html,'lxml')

        authenticity_token = re.search(r'name="authenticity_token" value="(.+?)"', html).group(1)
        print('authenticity_token:', authenticity_token)
        # at = soup.select('input[name="authenticity_token"]')[0]
        # print(at)

        # ui_metrics = re.search(r'name="ui_metrics" value="(.+?)"', html).group(1)
        # ui_metrics = soup.select('input[name="ui_metrics"]')
        # for u in ui_metrics:
        #     print('ui_metrics:', u)

        payload = {'session[username_or_email]': username,
                   'session[password]': password,
                   'authenticity_token': authenticity_token,
                   'scribe_log':'',
                   'remember_me': '1',
                   'redirect_after_login': '',
                   }
        # userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
        # headers = {'User-Agent': userAgent,
        #            'Accept-Encoding': 'gzip, deflate, br',
        #            'Accept-Language': 'zh-CN,zh;q=0.8',
        #            'X-Requested-With': 'XMLHttpRequest'}
        url = 'https://twitter.com/sessions'
        try:
            # print('http requests ing ... ', url)
            res = loginSession.post(url, verify=False, headers=self.headers, data=payload, timeout=30, allow_redirects=True)
            # print('http requests done ... ', res.url)
        except Exception as e:
            print(Exception('My NetERR', e))
            return None

        req_cookie = requests.utils.dict_from_cookiejar(loginSession.cookies)

        # print(req_cookie)

        loginSession.close()
        return req_cookie

    def get_proxyEnable(self,host,user):
        conn = pymongo.MongoClient(host=host,port=27017)
        db = conn['twitter']
        coll = db['twitter_account']
        for doc in coll.find():
            if doc['user'] == user:
                proxyEnable = doc['proxyEnable']
                return proxyEnable


if __name__ == "__main__":
    conn = MongoClient('10.1.18.93', 27017)
    db = conn['twitter']
    cookies_collection = db['twitter_cookies']
    # test = Fetcher('dnkw45915878ken@163.com',"cloud335335")#2
    # test = Fetcher('y53677311luboxio@163.com',"cloud335335")#2
    # test = Fetcher('skxs55899248che@163.com',"cloud335335")#2
    # test = Fetcher('Oll6907573taoy@163.com',"cloud335335")#2
    # test = Fetcher('oko7190962ta@163.com',"cloud335335")#1
    # test = Fetcher('13588828653@163.com',"cloud335335")#2
    # test = Fetcher('z.798818344@163.com',"jxi'llfynow")#1
    # test = Fetcher('wx_13588828653@sina.com', "cloud323323")#1
    # test = Fetcher('wx_13588828653@126.com','cloud323323')#2
    # test = Fetcher('wx_hu@139.com', "cloud323323")#2
    # test = Fetcher('cloud_335@yeah.net', "cloud323323")#2
    # test = Fetcher('cloud_323@sohu.com',"cloud323323")#2
    # test = Fetcher('wx_hdu@outlook.com',"cloud323323")#1
    # test = Fetcher('hdu_wx@hotmail.com',"cloud323323")#2
    # test = Fetcher('TrORWkwfTu0812G',"cloud335335")#2
    # test = Fetcher('yYm07V0Glu4YYAe', "cloud335335")#2
    # test = Fetcher('RoiuExT0Uq9PgO8','cloud335335')#2
    # test = Fetcher('NF1R3gUV6oYMqDN','cloud335335')#2
    # test = Fetcher('Nd14MzqVRvIp5wz','cloud335335')#2
    # test = Fetcher('ic4u9sHr6KnrLJq','cloud335335')#1
    # test = Fetcher('6nJotwM75l06NA9','cloud335335')#2
    # test = Fetcher('IAr6DbVLUa9S3sX','cloud335335')#2


    #2019-01-02新买账号
    # test = Fetcher('Gavin29521135','mwuxEVoCIa')  #2
    # test = Fetcher('Michael86513789','zGKk06oSZ1') #1
    # test = Fetcher('Anthony05154625','McnU5DiHPY')#1
    # test = Fetcher('mic_trevor','jnsa87hBHm')     #2
    # test = Fetcher('Juan80505150','g8gSpBJ2bc')   #1
    # test = Fetcher('Jayden62596535','ATuAFOeR8K')   #2
    # test = Fetcher('Noah36915356','yd6kS2C8ew') #2
    # test = Fetcher('Jacob74135082','b6WG8RHG0S')    #1
    # test = Fetcher('Joshua17330664','ibmLwlXc7B')   #2
    # test = Fetcher('CleggHomerus','ZKKVM2smwu')       #1
    # test = Fetcher('NF1R3gUV6oYMqDN','cloud335')    #1
    # test = Fetcher('cn8tG3vWZmBvA62','cloud335')    #2
    #2019-01-04新买账号
    # test = Fetcher('hamilton_newark','v1sD123xgI')      #2
    # test = Fetcher('AshbrookeHamlen', '5IJ0GrY1yT')#1
    # test = Fetcher('LarsMchattie', 'bJHt4pM0Zg')    #1
    # test = Fetcher('MarleyShepperd', 'HtgBZ6X2z5')#2
    # test = Fetcher('ArchaimbaudChi3', 'oske8HI7BM')#1
    # test = Fetcher('BarnabePaston', 'me8R4h1UFE')#1
    # test = Fetcher('OgdanPeterson', '2DvQlmrr7F')#2
    # test = Fetcher('ButlingGoddard', 'ajICNRwPiw')    #2
    # test = Fetcher('ElvridgeVasili', 'mQLuvuHd1c')#1
    # test = Fetcher('BennettSinpson', 'TySw0N5Tbd')#2

    #2019-01-10
    # test = Fetcher('RusselArtus','FKLNntAb0T')    #1
    # test = Fetcher('ClaibornDickins', 'PlSFrSPjKj')#2
    # test = Fetcher('AlvieThistletw1', 'IR4DeGC4dd')#1
    # test = Fetcher('SigvardSpurgeon', '6SrRTFFVVa')#1
    # test = Fetcher('HillierHocking', 'cOqe2WxX8G')#1
    # test = Fetcher('JimmieDuxbury', '1nIenuez1C')#1
    # test = Fetcher('GaultieroTedfo1', 'EZwm4MPfUd')
    # test = Fetcher('BradenHarwood', 'kmQQRleknr')
    # test = Fetcher('HambyTremain', 'M2EjPeki9a')



    url = 'https://twitter.com/ctba/followers/users?include_available_features=1&include_entities=1&max_position=-1&reset_error_state=false'
    test = Fetcher()
    host = sys.argv[1]
    myclient = pymongo.MongoClient(host,27017)
    db = myclient
    cookie = test.login()

    res = requests.get(url,headers=out_headers,timeout=30,allow_redirects=False, cookies=cookie)



