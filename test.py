import pymongo
import requests
import re
import json
import os

session = requests.session()
"""
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/skillCategory?includeHiddenEndorsers=True
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/browsemapWithDistance
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/profileContactInfo
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/+ experience_id + "/positionGroups?start=0&count=" + str(experience_count)
https://www.linkedin.com/voyager/api/identity/profiles/screen_name/
"""


class Fetcher(object):
    def __init__(self):
        self.loginUrl = 'https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin'
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "content-type": "application/json",
            'Host': 'www.linkedin.com',
            'Referer': 'https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin'
        }
        self.loginheaders = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            # "content-type": "application/x-www-form-urlencoded",
            'Host': 'www.linkedin.com',
            # 'Referer': 'https://www.linkedin.com/home'
        }

    def login(self, username, password):
        try:
            print('http requests ing ... ', self.loginUrl)
            res = session.get(self.loginUrl, verify=False, timeout=30, allow_redirects=False)
            print('http requests done ... ', res.url)
        except Exception as e:
            print(e)
            return None
        html = res.text
        print(html)
        loginCsrfParam = re.search(r'type="hidden" name="loginCsrfParam" value="(.+?)"', html).group(1)
        csrfToken = re.search(r'type="hidden" name="csrfToken" value="(.+?)"', html).group(1)
        sIdString = re.search(r'type="hidden" name="sIdString" value="(.+?)"', html).group(1)
        controlId = re.search(r'type="hidden" name="controlId" value="(.+?)"', html).group(1)
        parentPageKey = re.search(r'type="hidden" name="parentPageKey" value="(.+?)"', html).group(1)
        pageInstance = re.search(r'type="hidden" name="pageInstance" value="(.+?)"', html).group(1)
        trk = re.search(r'type="hidden" name="trk" value="(.+?)"', html).group(1)
        payload = {
            'session_key': username,
            'session_password': password,
            'loginCsrfParam': loginCsrfParam,
            'csrfToken': csrfToken,
            'sIdString': sIdString,
            'controlId': controlId,
            'parentPageKey': parentPageKey,
            'pageInstance': pageInstance,
            'trk': trk,
        }
        url = 'https://www.linkedin.com/checkpoint/lg/login-submit'
        try:
            print('http requests ing ... ', url)
            res = session.post(url, verify=False, headers=self.loginheaders, data=payload, timeout=30,
                               allow_redirects=True)
            print('http requests done ... ', res.url)
        except Exception as e:
            print(Exception('My NetERR', e))
            return None
        req_cookie = requests.utils.dict_from_cookiejar(session.cookies)
        session.close()
        return req_cookie

requests.packages.urllib3.disable_warnings()
if __name__ == "__main__":
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
        'x-li-deco-include-micro-schema': 'true',
        'x-li-lang': 'zh_CN',
        #'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;vLsbIDGVRoyljdLMVTeeOw==',
        'x-li-track': '{"clientVersion":"1.7.1305","osName":"web","timezoneOffset":8,"deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1920,"displayHeight":1080}',
        'x-restli-protocol-version': '2.0.0',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'www.linkedin.com',
        'Referer': 'https://www.linkedin.com/in/%E9%95%B7%E4%B8%89-%E4%B8%80%E4%B8%98-b41448149/'
    }

    test = Fetcher()
    # cookie = test.login("861959219@qq.com", "19971109.Jzmy")
    if not os.path.isfile("cookie.json"):
        cookie = test.login("861959219@qq.com", "19971109.Jzmy")
        print(cookie)
        with open("cookie.json", 'w') as f:
            json.dump(cookie, f)
    else:
        with open("cookie.json", 'r') as f:
            cookie = json.load(f)
    # print(eval(cookie["JSESSIONID"]))
    header["csrf-token"] = eval(cookie["JSESSIONID"])
    url='https://www.linkedin.com//voyager/api/identity/profiles/wallaeysmichael/browsemapWithDistance'
    url1='https://www.linkedin.com/voyager/api/identity/profiles/jay-w-kim-496aa438/skillCategory?includeHiddenEndorsers=true'
    url2='https://www.linkedin.com/voyager/api/messaging/presenceStatuses'
    url3='https://www.linkedin.com/voyager/api/identity/profiles/alex-kong-yuk-tsung/browsemapWithDistance'
    url4='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=%E5%B0%8F%E4%B8%BD-%E9%99%88-55a287176&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    url5='{"GET":{"scheme":"https","host":"www.linkedin.com","filename":"/voyager/api/identity/profiles/cameron-evans-9753795/recommendations","query":{"q":"given"},"remote":{"地址":"127.0.0.1:10809"}}}'

    url6='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=alex-kong-yuk-tsung&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    url7='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=1johnnyg&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    url8='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=cameron-evans-9753795&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    url9='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=dharmesh&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    url10='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=qianyizhen&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    course='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=matthew-rowland-5193b5159&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    pub_pro_patent='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=dpatil&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    rec_received='https://www.linkedin.com/voyager/api/identity/profiles/dpatil/recommendations?q=received&recommendationStatuses=List(VISIBLE)'
    rec_given='https://www.linkedin.com/voyager/api/identity/profiles/dpatil/recommendations?q=given'
    rec_given_next='https://www.linkedin.com/voyager/api/identity/profiles/ACoAAABLSOkBtiGumBezd8WnBcKO9WU4_9xZBo0/recommendations?count=5&q=given&start=10'
    receibed_tagurl='https://www.linkedin.com/voyager/api/identity/profiles/bernardmarr/recommendations?q=received&recommendationStatuses=List(VISIBLE)'
    member='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=dpatil&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    recent_activity='https://www.linkedin.com/voyager/api/identity/profiles/dpatil/recentActivities'
    alex_member='https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity=alex-kong-yuk-tsung&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-57'
    recent_activity_1='https://www.linkedin.com/voyager/api/identity/profileUpdatesV2?count=5&includeLongTermHistory=true&moduleKey=member-activity%3Aphone&paginationToken=dXJuOmxpOmFjdGl2aXR5OjY3MDI2MDAzNTY4NTkyNzMyMTYtMTU5ODAyNDQ0Mzg5NA%3D%3D&profileUrn=urn%3Ali%3Afsd_profile%3AACoAAABLSOkBtiGumBezd8WnBcKO9WU4_9xZBo0&q=memberFeed&start=35'
    inster_folow='https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables=%7B%22id%22%3A%224055534935%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Atrue%2C%22first%22%3A24%7D'
    response = session.get(url=inster_folow, headers=header, cookies=cookie)
    # print(response.url)
    # print(response.text)
    # print(response.status_code)
    shuju_=response.text
    # result=json.dumps(shuju_)
    with open("inster_follow.txt", 'w',encoding='UTF-8') as f:
        f.write(shuju_)

    # print(shuju_)
