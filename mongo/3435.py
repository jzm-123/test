import logging

import requests
def dict_from_cookiejar(cj):
    cookie_dict = {}
    for cookie in cj:
        cookie_dict[cookie.name] = cookie.value
    return cookie_dict

BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
STORIES_UA = 'Instagram 123.0.0.21.114 (iPhone; CPU iPhone OS 11_4 like Mac OS X; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/605.1.15'
CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
out_headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Host": "www.instagram.com",
               }

BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
STORIES_UA = 'Instagram 123.0.0.21.114 (iPhone; CPU iPhone OS 11_4 like Mac OS X; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/605.1.15'
CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
class Fetcher(object):
    def __init__(self, username, pwd):
        self.login_user = username
        self.login_pass = pwd
        self.session = requests.Session()
        self.session.headers = {'user-agent': CHROME_WIN_UA}
        self.cookies = ''
    def login(self):
        """Logs in to instagram."""
        self.session.headers.update({'Referer': BASE_URL, 'user-agent': STORIES_UA})
        req = self.session.get(BASE_URL)

        self.session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})

        login_data = {'username': self.login_user, 'password': self.login_pass}
        login = self.session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        self.session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        self.cookies = dict_from_cookiejar(login.cookies)
    def login_proxy(self,proxies):
        """Logs in to instagram."""
        self.session.proxies=proxies
        self.session.headers.update({'Referer': BASE_URL, 'user-agent': STORIES_UA})
        req = self.session.get(BASE_URL)

        self.session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})

        login_data = {'username': self.login_user, 'password': self.login_pass}
        login = self.session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        self.session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        self.cookies = dict_from_cookiejar(login.cookies)
if __name__ == '__main__':
    url = 'https://instagram.com/jaychou/'
    logging.basicConfig(filename="instagram_cookie.log", level=logging.DEBUG)
    test = Fetcher("16.52599079", "19971109.Jzmy")
    test.login()
    cookie = test.cookies
    print(cookie)
    logging.debug('cookie:', cookie)
    res = requests.get(url, headers=out_headers, timeout=30, allow_redirects=False, cookies=cookie)
    logging.debug(res.status_code)