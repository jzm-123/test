import json
import re
with open('shuju6.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
elements = data["elements"][0]
organization=[]
for item in elements["profileOrganizations"]["elements"]:
    organization_item={}
    if "name" in item.keys():
        organization_item["organization_name"]=item["name"]
    if "dateRange" in item.keys():
        if"start" in item["dateRange"].keys():
            if "month" in item["dateRange"]["start"]:
                organization_item["organization_startTime"]=str(item["dateRange"]["start"]["year"])+'-'+str(item["dateRange"]["start"]["month"])
            else:
                organization_item["organization_startTime"] = str(item["dateRange"]["start"]["year"])
        if"end" in item["dateRange"].keys():
            if "month" in item["dateRange"]["end"]:
                organization_item["organization_endTime"]=str(item["dateRange"]["end"]["year"])+'-'+str(item["dateRange"]["end"]["month"])
            else:
                organization_item["organization_endTime"] = str(item["dateRange"]["end"]["year"])
    if "description" in item.keys():
        organization_item["ororganization_description"]=item["description"]
    if "positionHeld" in item.keys():
        organization_item["ororganization_position"]=item["positionHeld"]
    organization.append(organization_item)
print(organization)
a=json.dumps(organization)
with open("test112.txt", 'w') as f:
    f.write(a)
