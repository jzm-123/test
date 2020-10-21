import json
with open('pub_pro_patent.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
"""
title
issuer
applicationNumber
description
filingDate
"""
elements=data["elements"][0]
# patentment={"title":[],"issuer":[],"issueDate":[],"applicationNumber":[],"description":[],"filingDate":[]}
patent=[]
for item in elements["profilePatents"]["elements"]:
    patentment={}
    if "title" in item.keys():
        patentment["title"]=item["title"]
    if "issuer" in item.keys():
        patentment["issuer"]=item["issuer"]
    if "issuedOn" in item.keys():
        if "month" and "day" in item["issuedOn"].keys():
            patentment["issueDate"]=str(item["issuedOn"]["year"])+"-"+str(item["issuedOn"]["month"])+"-"+str(item["issuedOn"]["day"])
        elif "month" in item["issuedOn"].keys() and "day" not in item["issuedOn"].keys():
            patentment["issueDate"] = str(item["issuedOn"]["year"]) + "-" + str(item["issuedOn"]["month"])
        else:
            patentment["issueDate"] = str(item["issuedOn"]["year"])
    if "filedOn" in item.keys():
        if "month" and "day" in item["filedOn"].keys():
            patentment["filingDate"]=str(item["filedOn"]["year"])+"-"+str(item["filedOn"]["month"])+"-"+str(item["filedOn"]["day"])
        elif "month" in item["filedOn"].keys() and "day" not in item["filedOn"].keys():
            patentment["filingDate"] = str(item["filedOn"]["year"]) + "-" + str(item["filedOn"]["month"])
        else:
            patentment["filingDate"] = str(item["filedOn"]["year"])
    if "applicationNumber" in item.keys():
        patentment["applicationNumber"]=item["applicationNumber"]
    if "description" in item.keys():
        patentment["description"]=item["description"]
    patent.append(patentment)
    a=json.dumps(patent)
with open("test112.txt", 'w') as f:
    f.write(a)
print(patent)