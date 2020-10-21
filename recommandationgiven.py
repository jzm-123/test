"""
recommendee
occupation
relationship
created
recommendationText
"""
from datetime import datetime
import  re
import time
import json
with open("rec_given_next.txt","r",encoding="UTF-8") as f:
    data=json.load(f)
elements=data["elements"]
givedRecommendation=[]
for item in elements:
    givedRecommendation_item={}
    if "created" in item.keys():
        t=item["created"]
        timeStamp = float(t / 1000)  # 毫秒时间戳转为秒级时间戳
        timeArray = time.localtime(timeStamp)  # float变为时间戳
        real_time = time.strftime("%Y-%m-%d", timeArray)  # 时间戳转成Y-M-D的str
        givedRecommendation_item["created"]=real_time
    if "recommendee" in item.keys():
        if "firstName" and "lastName" in item["recommendee"].keys():
            givedRecommendation_item["recommendeeName"]=item["recommendee"]["firstName"]+" "+item["recommendee"]["lastName"]
        if "occupation" in item["recommendee"].keys():
            givedRecommendation_item["recommendeeOccupation"]=item["recommendee"]["occupation"]
    if "relationship" in item.keys():
        givedRecommendation_item["relationship"]=item["relationship"]
    if "recommendationText" in item.keys():
        givedRecommendation_item["recommendationText"]=item["recommendationText"]
    givedRecommendation.append(givedRecommendation_item)
    if "entityUrn" in item.keys():
        url_trans=item["entityUrn"]
        url_=url_trans.split(",")[-3]
        url=url_.split("(")[-1]
        givedRecommendation_item["url"]=url
        # print(url)
# print(givedRecommendation_item["url"])
url_trans=data["elements"][0]["entityUrn"]
url_=url_trans.split(",")[-3]
url=url_.split("(")[-1]
givedRecommendation_item["url"]=url
total=data["paging"]["total"]
pages=int((11-10)/5)
print(url)
print(pages)
print(total)
a = json.dumps(givedRecommendation)
with open("test111.txt", 'w') as f:
    f.write(a)