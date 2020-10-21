print('http requests ing ... ', self.loginUrl)
test_url = "https://www.instagram.com/accounts/login/"
res = loginSession.get(
    test_url, verify=False, timeout=5, allow_redirects=True)
print('http requests done ... ', res.url)