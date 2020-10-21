import json
with open("shuju10.txt","r",encoding="UTF-8") as f:
    data=json.load(f)
# volunteerment={"volunteer_companyName":[],"role":[],"description":[],"startDate":[],"endDate":[]}
elements=data["elements"][0]
volunteer=[]
for item in elements["profileVolunteerExperiences"]["elements"]:
    volunteerment = {}
    if "role" in item.keys():
        volunteerment["role"]=item["role"]
    if "companyName" in item.keys():
        volunteerment["volunteer_companyName"]=item["companyName"]
    if "dateRange" in item.keys():
        if "start" in item["dateRange"].keys():
            if "month" in item["dateRange"]["start"]:
                volunteerment["startDate"]=str(item["dateRange"]["start"]["year"]) + "-" + str(item["dateRange"]["start"]["month"])
            else:
                volunteerment["startDate"] = str(item["dateRange"]["start"]["year"])
        if "end" in item["dateRange"].keys():
            if "month" in item["dateRange"]["end"]:
                volunteerment["endDate"]=str(item["dateRange"]["end"]["year"]) + "-" + str(item["dateRange"]["end"]["month"])
            else:
                volunteerment["endDate"] = str(item["dateRange"]["end"]["year"])
    if "description" in item.keys():
        volunteerment["description"]=item["description"]
    volunteer.append(volunteerment)
print(type(volunteerment["description"][0]))
a=json.dumps(volunteer)
with open("test111.txt", 'w') as f:
    f.write(a)
print(volunteer)
