import pymongo
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    '192.168.200.82',
    ssh_username="root",
    ssh_password="xietong123",
    remote_bind_address=('127.0.0.1', 27017)
)

server.start()

cookies=[b'csrftoken=vOPB2lcdMb0BlNZqRnAXRieNnxFxIDln; ds_user_id=42541271187;rur=FRC; sessionid=42541271187%3AyNdmt1Jxa7RtVb%3A0; csrftoken=vOPB2lcdMb0BlNZqRnAXRieNnxFxIDln; ds_user_id=42541271187;rur=FRC;sessionid=42541271187%3AyNdmt1Jxa7RtVb%3A0; ig_did=01E3B7FF-C6A9-43E1-8C37-AA8C0E94F1CA']

cookie = cookies[0].decode('utf-8')
# print(cookie)
cookieDict = {}
items = cookie.split(";")
# print(items)
'Whitesarah5774105'
conn = pymongo.MongoClient("127.0.0.1", server.local_bind_port)
db = conn['instagram']
coll = db['instagram_account']
for doc in coll.find():
    if doc['user'] == 'Whitesarah5774105':
        print(doc['imgVisits'])
server.stop()