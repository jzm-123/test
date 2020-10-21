import json
import re
with open('shuju6.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
elements = data["elements"][0]
testScore=[]
for item in elements["profileTestScores"]["elements"]:
    testScore_item={}
    if "score" in item.keys():
        testScore_item["test_score"]=item["score"]
    if "name" in item.keys():
        testScore_item["test_score_name"]=item["name"]
    if "dateOn" in item.keys():
        if "month" in item["dateOn"].keys():
            testScore_item["test_score_time"]=str(item["dateOn"]["year"])+"-"+str(item["dateOn"]["month"])
        else:
            testScore_item["test_score_time"]=str(item["dateOn"]["year"])
    testScore.append(testScore_item)
    a=json.dumps(testScore)
with open("test111.txt", 'w') as f:
    f.write(a)
print(testScore)