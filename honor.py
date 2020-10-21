import json
import re
with open('shuju6.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
elements = data["elements"][0]
honor=[]
for item in elements["profileHonors"]["elements"]:
    honor_item={}
    if "title" in item.keys():
        honor_item["honor_title"]=item["title"]
    if "issuer" in item.keys():
        honor_item["honor_issuer"]=item["issuer"]
    if "issuedOn" in item.keys():
        if "month" in item["issuedOn"].keys():
            honor_item['honor_issueTime']=str(item["issuedOn"]["year"])+"-"+str(item["issuedOn"]["month"])
        else:
            honor_item['honor_issueTime']=str(item["issuedOn"]["year"])
    honor.append(honor_item)
print(honor)