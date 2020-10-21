import redis
import json
import time

# r = redis.Redis(host='127.0.0.1',port='6379')
# result = {'user_id': '846457158233313280', 'nick_name': '規制氏(雑魚)', 'verified': False, 'screen_name': 'qpebfoidkpvqr71', 'desc': '敦盛に習うとすれば、既に半分は過ぎた事になるが成りたい様には全く至ってないと思う。佐々成政も言ってます、全く意地ぐらいは不便ながらも通したいものです。ちなみに幽香好の端くれです！最近はシンフォギアＧが一押し。クリスちゃん本当最高やで', 'location': '', 'site': None, 'join_date': '1:21 PM - 27 Mar 2017', 'tweets': 5, 'following': 31, 'followers': 1, 'favorites': 0, 'lists': 0}
# result1 =  {'user_id': '846527804413923328', 'nick_name': '楊天天', 'verified': False, 'screen_name': 'xdleNAAlC14Tmu2', 'desc': None, 'location': '', 'site': None, 'join_date':
#  '下午6:02 - 2017年3月27日', 'tweets': 34, 'following': 100, 'followers': 2, 'favorites': 0, 'lists': 0}

# value = json.dumps(result)
# r.lpush('location:key',value)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


