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
print(cookie)
cookieDict = {}
items = cookie.split(";")
print(items)
# for item in items:
#     key = item.split('=')[0].replace(' ', '')
#     value = item.split('=')[1]
#     cookieDict[key] = value
# conn = pymongo.MongoClient("127.0.0.1", server.local_bind_port)
# db = conn['instagram']
# coll = db['instagram_account']
# for doc in coll.find():
#     if doc['cookie']['sessionid'] == cookieDict['sessionid']:
#         print(doc['user'])

# class MongoUtils(object):
#     def __init__(self):
#         self.conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#         self.db = self.conn['linkedin']
#         self.db_account = self.db['linkedin_account']
#         self.db_job=self.db['linkedin_job']
#         # get the job db
#     def get_userinfo_db(self, job_id):
#         job_id_search = {"_id": job_id}
#         result=self.db_job.find_one(job_id_search)
#         if result is None:
#             return
#         else:
#             userinfo_id=[]
#             job_name=result["name"]
#             userinfo_db=self.db["linkedin_userinfo"+'/'+str(job_id)+'/'+str(job_name)]
#             for x in userinfo_db.find():
#                 userinfo_id.append(x["user_id"])
#             return userinfo_id
# 
#     def get_friend_db(self, job_id):
#         job_id_search = {"_id": job_id}
#         result = self.db_job.find_one(job_id_search)
#         if result is None:
#             return
#         else:
#             friend_id = []
#             job_name = result["name"]
#             friend_db = self.db["linkedin_friends" + '/' + str(job_id) + '/' + str(job_name)]
#             # friend_db = self.db["linkedin_friends/1065/jin-jhon-837076193-8.12"]
#             for x in friend_db.find():
#                 friend_id.append(x["friends_id"])
#             return friend_id
# 
#     def get_company_db(self, job_id):
#         job_id_search = {"_id": job_id}
#         result=self.db_job.find_one(job_id_search)
#         if result is None:
#             return
#         else:
#             company_id=[]
#             job_name=result["name"]
#             company_db=self.db["linkedin_company"+'/'+str(job_id)+'/'+str(job_name)]
#             # company_db = self.db["linkedin_company/1065/jin-jhon-837076193-8.12"]
#             for x in company_db.find():
#                 company_id.append(x["company_id"])
#             return company_id
# mongo_class=MongoUtils()
# userinfo_name=mongo_class.get_userinfo_db(7200)
# friend_name=mongo_class.get_friend_db(7200)
# company_name=mongo_class.get_company_db(7200)
#get the userinfo db




#get the userinfo db
# def get_userinfo_db(job_id):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result=db_job.find_one(job_id_search)
#     if result is None:
#         return
#     else:
#         job_name=result["name"]
#         userinfo_db=db["twitter_userinfo"+'/'+str(job_id)+'/'+str(job_name)]
#         return userinfo_db
# 
# # userinfo duplication by UserId
# def findByUserId_userinfo(job_id,user_id):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result=db_job.find_one(job_id_search)
#     if result is None:
#         return None
#     else:
#         job_name=result["name"]
#         userinfo_db=db["twitter_userinfo"+'/'+str(job_id)+'/'+str(job_name)]
#         if userinfo_db.find({'user_id': user_id}).count() != 0:
#             return True
#         else:
#             return False
# 
# #get the tweets db
# def get_tweets_db(job_id):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result = db_job.find_one(job_id_search)
#     if result is None:
#         return None
#     else:
#         job_name = result["name"]
#         tweets_db = db["twitter_tweets" + '/' + str(job_id) + '/' + str(job_name)]
#         return tweets_db
# 
# # tweets duplication by ItemId
# def findByItemId_tweets(job_id,itemId):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result = db_job.find_one(job_id_search)
#     if result is None:
#         return False
#     else:
#         job_name = result["name"]
#         tweets_db =db["twitter_tweets" + '/' + str(job_id) + '/' + str(job_name)]
#         if tweets_db.find({'itemId': itemId}).count() != 0:
#             return True
#         else:
#             return False
# 
# # get the following db
# def get_following_db(job_id):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result = db_job.find_one(job_id_search)
#     if result is None:
#         return None
#     else:
#         job_name = result["name"]
#         following_db = db["twitter_following" + '/' + str(job_id) + '/' + str(job_name)]
#         return following_db
# 
# # following duplication by AttentionId
# def findByAttentionId_following(job_id,attention_id):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result=db_job.find_one(job_id_search)
#     if result is None:
#         return None
#     else:
#         job_name=result["name"]
#         following_db=db["twitter_following"+'/'+str(job_id)+'/'+str(job_name)]
#         if following_db.find({'attention_id': attention_id}).count() != 0:
#             return True
#         else:
#             return False
# 
# # get the follow db
# def get_follow_db(job_id):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result = db_job.find_one(job_id_search)
#     if result is None:
#         return None
#     else:
#         job_name = result["name"]
#         follow_db = db["twitter_follow" + '/' + str(job_id) + '/' + str(job_name)]
#         return follow_db
# 
# # follow duplication by fan_id
# def findByFanId_follow(job_id,fan_id,user_id):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result=db_job.find_one(job_id_search)
#     if result is None:
#         return None
#     else:
#         job_name=result["name"]
#         follow_db=db["twitter_follow"+'/'+str(job_id)+'/'+str(job_name)]
#         if follow_db.find({'fan_id': fan_id,'user_id': user_id}).count() != 0:
#             return True
#         else:
#             return False
# 
# # get the comments db
# def get_comments_db(job_id):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result = db_job.find_one(job_id_search)
#     if result is None:
#         return None
#     else:
#         job_name = result["name"]
#         comments_db = db["twitter_comments" + '/' + str(job_id) + '/' + str(job_name)]
#         return comments_db
# 
# # comments duplication by cid_str
# def findByCid_str_comments(job_id,cid_str):
#     conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
#     db = conn['twitter']
#     db_job = db['twitter_job']
#     job_id_search = {"_id": job_id}
#     result=db_job.find_one(job_id_search)
#     if result is None:
#         return None
#     else:
#         job_name=result["name"]
#         comments_db=db["twitter_comments"+'/'+str(job_id)+'/'+str(job_name)]
#         if comments_db.find({'cid_str': cid_str}).count() != 0:
#             return True
#         else:
#             return False

#get the userinfo db
def get_userinfo_db(job_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result=db_job.find_one(job_id_search)
    if result is None:
        return
    else:
        job_name=result["name"]
        userinfo_db=db["facebook_userinfo"+'/'+str(job_id)+'/'+str(job_name)]
        return userinfo_db

# userinfo duplication by UserId
def findByUserId_userinfo(job_id,user_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result=db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name=result["name"]
        userinfo_db=db["facebook_userinfo"+'/'+str(job_id)+'/'+str(job_name)]
        if userinfo_db.find({'user_id': user_id}).count() != 0:
            return True
        else:
            return False

#get the like_relationship db
def get_like_db(job_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result = db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name = result["name"]
        like_db = db["facebook_like" + '/' + str(job_id) + '/' + str(job_name)]
        return like_db

# like_relation duplication by userid postid
def findByUserId_like_relationship(job_id,user_id,post_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result = db_job.find_one(job_id_search)
    if result is None:
        return False
    else:
        job_name = result["name"]
        like_db =db["facebook_like" + '/' + str(job_id) + '/' + str(job_name)]
        if like_db.find({'user_id': user_id,"post_id":post_id}).count() != 0:
            return True
        else:
            return False

# get the friends db
def get_friends_db(job_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result = db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name = result["name"]
        friends_db = db["facebook_friends" + '/' + str(job_id) + '/' + str(job_name)]
        return friends_db

# friends duplication by friendsid userid
def findByFriendsId_friends(job_id,friends_id,user_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result=db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name=result["name"]
        friends_db=db["facebook_friends"+'/'+str(job_id)+'/'+str(job_name)]
        if friends_db.find({'friends_id': friends_id,'user_id':user_id}).count() != 0:
            return True
        else:
            return False

# get the content db
def get_follow_db(job_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result = db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name = result["name"]
        content_db = db["facebook_content" + '/' + str(job_id) + '/' + str(job_name)]
        return content_db

# content duplication by post_id
def findByFanId_follow(job_id,post_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result=db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name=result["name"]
        content_db=db["facebook_content"+'/'+str(job_id)+'/'+str(job_name)]
        if content_db.find({'post_id': post_id}).count() != 0:
            return True
        else:
            return False

# get the comments db
def get_comments_db(job_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result = db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name = result["name"]
        comments_db = db["facebook_comments" + '/' + str(job_id) + '/' + str(job_name)]
        return comments_db

# comments duplication by cid_str
def findByCid_str_comments(job_id,comment_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['facebook']
    db_job = db['facebook_job']
    job_id_search = {"_id": job_id}
    result=db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name=result["name"]
        comments_db=db["facebook_comments"+'/'+str(job_id)+'/'+str(job_name)]
        if comments_db.find({'comment_id': comment_id}).count() != 0:
            return True
        else:
            return False
item={}
item["itemId"]='1305363725256335361'
print(findByFanId_follow(3051,878833299673628672,155814794))
# for item_index in item["itemId"]:
    # print( item_index)
# print(get_tweets_db(552))
# def parse():
#     if get_tweets_db(1694):
#             if item["itemId"] in get_tweets_db_data(1694):
#                 return None
#             else:
#                 return item
#     else:
#         return item

# print(parse())
# comments=get_comments_db_data(3227)
# follow=get_follow_db_data(6686)
# following=get_following_db_data(3227)
# userinfo=get_userinfo_db_data(3227)
# tweets=get_tweets_db_data(8138)
# print(comments)
# print('\n')
# print('\n')
# print(follow)
# print('\n')
# print('\n')
# print(following)
# print('\n')
# print('\n')
# print(tweets)
# print('\n')
# print('\n')
# print(userinfo)
# myclient = pymongo.MongoClient("127.0.0.1", server.local_bind_port)
# mydb = myclient["linkedin"]
# db_job = mydb['linkedin_job']
# job_id=3829
# job_id_search = {"_id": 3829}
# result=db_job.find_one(job_id_search)
# job_name=result["name"]
# userinfo_db=mydb["linkedin_userinfo"+"/"+str(job_id)+"/"+str(job_name)]
# userinfo_result=userinfo_db.find_one()
# userinfo_id=userinfo_result["user_id"]
# print(userinfo_id)

server.stop()