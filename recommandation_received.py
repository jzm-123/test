"""
recommender
occupation
relationship
created
recommendationText
"""
from datetime import datetime
import time
import json
with open("rec_received.txt","r",encoding="UTF-8") as f:
    data=json.load(f)
page=data["paging"]
elements=data["elements"]
receivedRecommendation=[]
for item in elements:
    receivedRecommendation_item={}
    if "created" in item.keys():
        t=item["created"]
        timeStamp = float(t / 1000)  # 毫秒时间戳转为秒级时间戳
        timeArray = time.localtime(timeStamp)  # float变为时间戳
        real_time = time.strftime("%Y-%m-%d", timeArray)  # 时间戳转成Y-M-D的str
        receivedRecommendation_item["created"]=real_time
    if "recommender" in item.keys():
        if "firstName" and "lastName" in item["recommender"].keys():
            receivedRecommendation_item["recommenderName"]=item["recommender"]["firstName"]+" "+item["recommender"]["lastName"]
        if "occupation" in item["recommender"].keys():
            receivedRecommendation_item["recommenderOccupation"]=item["recommender"]["occupation"]
    if "relationship" in item.keys():
        receivedRecommendation_item["relationship"]=item["relationship"]
    if "recommendationText" in item.keys():
        receivedRecommendation_item["recommendationText"]=item["recommendationText"]
    receivedRecommendation.append(receivedRecommendation_item)
url_trans = data["elements"][0]["entityUrn"]
url = url_trans.split(",")[-2]
total=data["paging"]["total"]
pages=int((total-10)/5)
print(url)
print(pages)
print(total)
a = json.dumps(receivedRecommendation)
with open("test111.txt", 'w') as f:
    f.write(a)