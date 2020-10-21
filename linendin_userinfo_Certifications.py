import json
import re
with open('alex_member.txt','r',encoding='UTF-8') as f:
    data=json.load(f)

elements = data["elements"][0]
# certificationment={"licenseNumber":[],"startDate":[],"endDate":[],"certification_name":[],"authority":[],"company_name":[]}
certification=[]
for item in elements["profileCertifications"]["elements"]:
    certificationment = {}
    if "dateRange" in item.keys():
        if "start" in item["dateRange"].keys():
            if "month" in item["dateRange"]["start"].keys():
                certificationment["startDate"] = str(item["dateRange"]["start"]["year"]) + "-" + str(item["dateRange"]["start"]["month"])
            else:
                certificationment["startDate"] =str(item["dateRange"]["start"]["year"])
        if "end" in item["dateRange"].keys():
            if "month" in item["dateRange"]["end"].keys():
                certificationment["endDate"] = str(item["dateRange"]["end"]["year"]) + "-" + str(item["dateRange"]["end"]["month"])
            else:
                certificationment["endDate"] = str(item["dateRange"]["end"]["year"])
    if "name" in item.keys():
        certificationment["certification_name"] = item["name"]
    if "multiLocaleLicenseNumber" in item.keys():
        certificationment["licenseNumber"] = item["multiLocaleLicenseNumber"]["en_US"]
    if "authority" in item.keys():
        certificationment["authority"] = item["authority"]
    if "name" in item["company"].keys():
        certificationment["company_name"] = item["company"]["name"]
    certification.append(certificationment)
a = json.dumps(certification)
with open("test111.txt", 'w') as f:
    f.write(a)
print(certification)

