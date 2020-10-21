import pymongo
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    '192.168.200.82',
    ssh_username="root",
    ssh_password="xietong123",
    remote_bind_address=('127.0.0.1', 27017)
)


server.start()
#get the tweets db
def get_tweets_db(job_id):
    conn = pymongo.MongoClient("127.0.0.1",server.local_bind_port)
    db = conn['twitter']
    db_job = db['twitter_job']
    job_id_search = {"_id": job_id}
    result = db_job.find_one(job_id_search)
    if result is None:
        return None
    else:
        job_name = result["name"]
        tweets_db = db["twitter_tweets" + '/' + str(job_id) + '/' + str(job_name)]
        # if tweets_db:
        #     return True
        # else:
        #     return False
        return tweets_db

def findByItemId(job_id,itemId):
    conn = pymongo.MongoClient("127.0.0.1", server.local_bind_port)
    db = conn['twitter']
    db_job = db['twitter_job']
    job_id_search = {"_id": job_id}
    result = db_job.find_one(job_id_search)
    if result is None:
        return False
    else:
        job_name = result["name"]
        tweets_db =db["twitter_tweets" + '/' + str(job_id) + '/' + str(job_name)]
        print(tweets_db)
        if tweets_db.find({'itemId' :itemId}).count()!=0 :
            return True
        else:
            return False
item={}
item["itemId"]='1305023147440308225'
x=findByItemId(7728,item["itemId"])
jobid='286'
print(get_tweets_db(int(jobid)))
print(x)
# if findByItemId(9995,1):
    # print(1)
# else:
    # print(2)
server.stop()