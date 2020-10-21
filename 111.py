import pymongo
import requests
import re
import json
import os
session = requests.session()
loginUrl='https://www.instagram.com/accounts/login/'
res = session.get(loginUrl, verify=False, timeout=30, allow_redirects=False)
html = res.text
print(html)
with open('html.txt','w',encoding='UTF-8') as f:
    f.write(html)
loginCsrfParam = re.search(r'type="hidden" name="loginCsrfParam" value="(.+?)"', html).group(1)
csrfToken = re.search(r'type="hidden" name="csrfToken" value="(.+?)"', html).group(1)
sIdString = re.search(r'type="hidden" name="sIdString" value="(.+?)"', html).group(1)
controlId = re.search(r'type="hidden" name="controlId" value="(.+?)"', html).group(1)
parentPageKey = re.search(r'type="hidden" name="parentPageKey" value="(.+?)"', html).group(1)
pageInstance = re.search(r'type="hidden" name="pageInstance" value="(.+?)"', html).group(1)
trk = re.search(r'type="hidden" name="trk" value="(.+?)"', html).group(1)
print(loginCsrfParam)
print(csrfToken)
print(controlId)
print(sIdString)
print(parentPageKey)
print(pageInstance)
print(trk)